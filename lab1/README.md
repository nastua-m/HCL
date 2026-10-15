# GPUs vs CPUs (lab 1: architecture and performance)
The goal of this lab is to develop a deeper understanding of the fundamental architectural differences between GPUs and CPUs and to observe how these differences impact performance.

## Tasks (system info)
1. GPU architecture: NVIDIA RTX PRO 4000 Blackwell (nvidia-smi)
2. No. SMs: 70 (https://www.techpowerup.com/gpu-specs/rtx-pro-4000-blackwell-workstation.c4279)
3. No. SPs: 8.960 (https://www.techpowerup.com/gpu-specs/rtx-pro-4000-blackwell-workstation.c4279)
4. CPU: Intel(R) Xeon(R) w3-2525 (lscpu)
5. No. threads CPU vs no. threads GPU: 16 vs 259072

## Tasks (performance)
1. Compile and run addition
    team2@hclab02:~/Desktop/new/gpu-programming$ nvcc addition.cu -o addition
    team2@hclab02:~/Desktop/new/gpu-programming$ ./addition 
    Vector addition of 50000 elements
    CUDA kernel launch with 196 blocks of 256 threads
    Test PASSED
    Done

2. Measure execution time GPU (hint: `cudaEvent_t start, stop;` \n `cudaEventCreate(&start);`)
    ~0.15ms for the GPU at 50000 elements
3. Implement CPU version
    for(int i = 0; i < numElements; i++)
    {
        CCpu[i] = h_A[i] + h_B[i];
    }
4. Measure execution time CPU
    ~0.16ms for the CPU at 50000 elements
5. Compare CPU and GPU execution with changing block sizes (as low and as high, e.g., 512, 2048, so that you can gather performance trends) and data sizes (up to and including 50 billion)
    (could only go up to 500000000)
    CPU: 
    50k:0,15
    500k:1,65
    5m:17,56
    50m:157,00
    500m:346,70
    GPU
    1024 threads per block:
    50k:0,15
    500k:0,18
    5m:0,3
    50m:1,17
    500m:11,5
    512 threads per block:
    50k:0,09
    500k:0,19
    5m: 0,27
    50m: 1,16
    500m: 11,86
    32 threads per block:
    50k: 0,16
    500k: 0,19
    5m: 0,22
    50m: 1,17
    500m:11,28
    
6. Plot measurements and speedups (block sizes and increasing data)
    todo
7. Compile and run race condition exercise
    they all passed due to the solutions being uplaod to github.. The idea was to use atomic functions
8. Pass the race condition test by identifying the bug in the _countAboveThreshold_ CUDA kernel and solving it.
    use atomic
## Wrap up and deliverables
1. Create blog post (or GitHub repo)
2. Describe main applications for GPUs (graphics and AI)
3. Showcase your experiments and speed ups achieved
4. Segway to architectural differences (describe CPU vs GPU during lab, cores, threads, and other specifics)
5. Showcase speed up experiments and describe differences (especially for today)
6. Discuss the race condition problem, how they might appear, and how they are usually treated.
7. Wrap up and conclude with what's next
