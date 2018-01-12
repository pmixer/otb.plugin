# Visual Object Tracking Benchmark Appendix
> Bridging python and matlab version of OTB

For visual tracking practioners and researchers. As Python version of the [benchmark](http://cvlab.hanyang.ac.kr/tracker_benchmark/) is easier to use but its plotting function is incomplete, matlab version is better at plotting but not everyone love it. You may use `converter.py` to help with the issue.

```Python
python converter.py
```



`benchmark_py` and `benchmark_mat` are placeholders and not executable if you do not configure them. Please download and configure
them from the corresponding urls:

+ Matlab version-[http://cvlab.hanyang.ac.kr/tracker_benchmark/v1.0/tracker_benchmark_v1.0.zip](http://cvlab.hanyang.ac.kr/tracker_benchmark/v1.0/tracker_benchmark_v1.0.zip)
+ Python version-[https://github.com/jwlim/tracker_benchmark](https://github.com/jwlim/tracker_benchmark)

Or modify `ORIGIN_PATH` and `EXPORT_PATH` to your configured benchmark results location.

In reference to:
```
@inproceedings{ WuLimYang13,
  Title = {Online Object Tracking: A Benchmark},
  Author = {Yi Wu and Jongwoo Lim and Ming-Hsuan Yang},
  Booktitle = {IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  Year = {2013}
}
```
