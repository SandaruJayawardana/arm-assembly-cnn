# Implementation of CNN Using Neon ARM Assembly 
## Introduction
> Aim of this project was to speed-up the calculation speed in Yolo-tiny CNN algorithm using ARM V8 assembly instructions. I was able to implement convolution and max-pool operations with zero padding, using the assembly instrauctions using Neon instructions. Single precision floating point operations were used and commented algorithm is available in 'InlineConvAndMaxPool.txt' file. I designed vectorized implementation to achieve the advantage of SIMD facility of the VPU and Neon coprocessors. I used specially vldmia, vmul. f32, vadd. f32, vfma. f32, vcmp.f32,vstr instructions from the Neon. The converter.py can be used to remove the comments and convert it compiler supportive inline C++ code. Used C++ is available in 'sample.cpp' file. GNU g++ compiler was used to compile the code with neaon coprocessor flag. Code was tested in Raspberry Pi 3B+ with Raspbian (32bit version). 

* __g++ -o -mfpu=neon-vfpv3 out sample.cpp__

### Implemented convolution and maxpool algorithm and used registers are shown in below (Siplified Version)

#### 1. Data Load Step 1

<img src="https://github.com/SandaruJayawardana/arm-assembly-cnn/blob/main/img/Data_load_step_1.PNG" alt="alt text" width="310" height="300">

#### 2. Data Load Step 2

<img src="https://github.com/SandaruJayawardana/arm-assembly-cnn/blob/main/img/Data_load_step_2.PNG" alt="alt text" width="310" height="300">

#### 3. Data Load Step 3

<img src="https://github.com/SandaruJayawardana/arm-assembly-cnn/blob/main/img/Data_load_step_3.PNG" alt="alt text" width="310" height="300">

#### Summary

<img src="https://github.com/SandaruJayawardana/arm-assembly-cnn/blob/main/img/Summarized Block Diagram.PNG" alt="alt text" width="310" height="450">
