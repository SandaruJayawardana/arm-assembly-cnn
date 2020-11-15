# Implementation of CNN Using Neon ARM Assembly 
## Introduction
> Aim of this project was to speed-up the calculation speed in Tiny YOLO CNN algorithm using ARM V8 assembly instructions. I was able to implement convolution and max-pool operations with zero padding, using the assembly instrauctions using Neon instructions. Single precision floating point operations were used and commented algorithm is available in 'InlineConvAndMaxPool.txt' file. I designed vectorized implementation to achieve the advantage of SIMD facility of the VPU and Neon coprocessors. I used specially vldmia, vmul. f32, vadd. f32, vfma. f32, vcmp.f32,vstr instructions from the Neon. The converter.py can be used to remove the comments and convert it compiler supportive inline C++ code. Used C++ is available in 'sample.cpp' file. GNU g++ compiler was used to compile the code with neaon coprocessor flag. Code was tested in Raspberry Pi 3B+ with Raspbian (32bit version). 


* __g++ -o -mfpu=neon-vfpv3 out sample.cpp__

### Implemented convolution and maxpool algorithm and used registers are shown in below (Siplified Version)

+ GNU g++ compiler pass the first 3 parameter values of a function in R1, R2, R3 registers. I used that to pass the necessary pointers to track the image, kernals and target for the each layer in the CNN.

#### 1. Data Load Step 1

<img src="https://github.com/SandaruJayawardana/arm-assembly-cnn/blob/main/img/Data_load_step_1.PNG" alt="alt text" width="310" height="300">

#### 2. Data Load Step 2

<img src="https://github.com/SandaruJayawardana/arm-assembly-cnn/blob/main/img/Data_load_step_2.PNG" alt="alt text" width="310" height="300">

#### 3. Data Load Step 3

<img src="https://github.com/SandaruJayawardana/arm-assembly-cnn/blob/main/img/Data_load_step_3.PNG" alt="alt text" width="310" height="300">

#### Summary

<img src="https://github.com/SandaruJayawardana/arm-assembly-cnn/blob/main/img/Summarized Block Diagram.PNG" alt="alt text" width="310" height="450">

## Results
> The code only executed in a single core (because it was not optimized for multi-core execution yet) and I estimated the total execution time for Tiny YOLO algorithm. It was around 2.8s (Estimation done with weighted manner with executing for each layer and didn't change any process priority). Tensorflow Lite gives around 0.8 FPS for Tony YOLO and equivelent execution time for one interation is around 1.25s. It seems that assembly implementation can gain some sort of improvement respect to the Tensorflow Lite. Project was disconituined beacuse of the lack resultant performance. 
