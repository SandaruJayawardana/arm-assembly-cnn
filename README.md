# Implementation of CNN Using Neon ARM Assembly 
## Introduction
> Aim of this project was to speed-up the calculation speed in Yolo-tiny CNN algorithm using ARM V8 assembly instructions. I was able to implement convolution and max-pool operations with zero padding, using the assembly instrauctions using Neon instructions. Commented algorithm is available in 'InlineConvAndMaxPool.txt' file and converter.py can be used to remove the comments and convert it compiler supportive inline code. Used C++ is available in 'sample.cpp' file. GNU g++ compiler was used to compile the code with neaon coprocessor flag. Code was tested in Raspberry Pi 3B+ with Raspbian (32bit version). 

#### g++ -o -mfpu=neon-vfpv3 out sample.cpp

### Implemented convolution and maxpool algorithm and used registers are shown in below

image: ![](https://github.com/SandaruJayawardana/arm-assembly-cnn/blob/main/img/Data_load_step_1.PNG) image.width 7
