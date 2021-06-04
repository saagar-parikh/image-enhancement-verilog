pout = imread('634_190x150_Gray.png');
pout_adapthisteq = adapthisteq(pout);
%montage({pout_adapthisteq},'Size',[1 1])
title("Original Image and Enhanced Images using Matlab")
pout_adapthisteq = imresize(pout_adapthisteq, size(pout));
imwrite(pout_adapthisteq,'634_matlab.png')
