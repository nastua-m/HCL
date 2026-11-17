# Deliverables week 1
by Anastasiia Matynkova and Michel Bruns
 
## Main applications of GPU: 
Parallelized workflows, eg.:
- training NN, 3D calculations such as simulations, rendering, Operating on large amounts of data.

## Experiments
These are the results of our benchmarks:
![](lab1/cpu_vs_gpu_benchmark.png)
As you can see, the CPU is much slower and as the plot is shown on a log scale, the gap between CPU and GPU performance gets wider as we increase input size.

## Architecture comparison
GPUs have multiple orders of magnitude more cores than CPUs, this allows the GPU to execute similar tasks in paralel and achieve a significant perfomance advantage as data input increases. GPUs have a different memory hiearchy.

For comparison:
| CPU | GPU |
|---|---|
| Intel Xeon w3-2525 | NVIDIA RTX PRO 4000 Blackwell |
| 16 threads | 143,360 threads |
| — | 70 SMs |
| — | 8,960 SPs |

## Race conditios
Race conditions occure when multiple threads try to write to the same piece of memory. This can be prevented by using atomic operations, or gating the used variables with semaphores or similar. 


---------------------------
# Deliverables week 4-6
by Anastasiia Matynkova and Michel Bruns

## Statistics task 1:

offload rate: 48%

traffic:~250KB speed: ~2KB/s

traffic offloaded: 24000 pictures

latency: 0.0045s

latency offloaded: 0.0053s


## Experience simulation:
We preprocessed the image like this:

1. Raw BGR Image

2. Perspective Warped Image

3. Grayscale Image

4. Blurred Image

And applied edge detection on top via:

5. Canny Edge Detection

6. Hough Lines probabilistic detection


After detection the lines, we fine tuned parameters such as speed and steering angle based on how much the car was off lane center and whether a left or right turn was coming up. To remove oversteering a moving average was used taking the previous error and the current error into account, both equally weighted. This removed the wiggling from left to right.
