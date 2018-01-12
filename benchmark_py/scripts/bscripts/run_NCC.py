import cv2
import numpy
import os
import time

class NCCTracker(object):

    def __init__(self, image, x, y, w, h):
        self.window = max(w, h) * 1.3

        left = max(x, 0)
        top = max(y, 0)

        right = min(x + w, image.shape[1] - 1)
        bottom = min(y + h, image.shape[0] - 1)

        self.template = image[int(top):int(bottom), int(left):int(right)]
        self.position = (x + w / 2, y + h / 2)
        self.size = (w, h)

    def track(self, image):

        left = max(round(self.position[0] - float(self.window) / 2), 0)
        top = max(round(self.position[1] - float(self.window) / 2), 0)

        right = min(round(self.position[0] + float(self.window) / 2), image.shape[1] - 1)
        bottom = min(round(self.position[1] + float(self.window) / 2), image.shape[0] - 1)

        if right - left < self.template.shape[1] or bottom - top < self.template.shape[0]:
            return vot.Rectangle(self.position[0] + self.size[0] / 2, self.position[1] + self.size[1] / 2, self.size[0], self.size[1])

        cut = image[int(top):int(bottom), int(left):int(right)]

        matches = cv2.matchTemplate(cut, self.template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(matches)

        self.position = (left + max_loc[0] + float(self.size[0]) / 2, top + max_loc[1] + float(self.size[1]) / 2)

        return (left + max_loc[0], top + max_loc[1], self.size[0], self.size[1])

def run_NCC(seq, rp, bSaveImage):
    '''
    Baseline algorithm based on template matching
    '''
    initFrame = cv2.imread(os.path.join(seq.path, seq.imgFormat.format(seq.startFrame)))
    tmp = seq.init_rect
    tracker = NCCTracker(initFrame, tmp[0], tmp[1], tmp[2], tmp[3])
    output = [tmp]

    t_begin = time.time()
    for i in range(seq.startFrame+1, seq.endFrame+1):
        newFrame = cv2.imread(os.path.join(seq.path, seq.imgFormat.format(i)))
        x, y, w, h = tracker.track(newFrame)
        # x, y, w, h = int(x), int(y), int(w), int(h)
        output.append([x, y, w, h])
        # if bSaveImage:
        #     if len(tracker.template.shape) == 3:
        #         bboxImage = cv2.rectangle(newFrame, (x, y), (x+w, y+h), (0,0,255))
        #     else:
        #         bboxImage = cv2.rectangle(newFrame, (x, y), (x+w, y+h), 0)
        #     savePath = os.path.join(rp, seq.name+'_'+seq.imgFormat.format(i))
        #     cv2.imwrite(savePath, bboxImage)

    t_end = time.time()

    res = {}
    res['type'] = 'rect'
    res['res'] = output
    res['fps'] = (seq.endFrame - seq.startFrame)/(t_end-t_begin)
    return res
