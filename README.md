# Enhancement of Night Vision IR Images using Verilog
Applying various image enhancement algorithms on Night Vision IR images using Xilinx Vivado.

Details about the file names in `filenames.txt`.

## Brief
**Aim:** To apply image enhancement algorithms on Night Vision infrared images using Xilinx Vivado.

**Algorithms used:**
1. Histogram Equalisation
2. Histogram Matching
3. Double Plateau Histogram Equalisation
4. Top Hat Transform

**Dataset:** [ir:iricra2014 – ASL Datasets](https://projects.asl.ethz.ch/datasets/doku.php?id=ir:iricra2014)

## Algorithms

### 1. Histogram Equalisation
* A contrast stretching algorithm with a mathematical function that uniformly stretches the image histogram.
* Calculate the  probability and cumulative distribution function(CDF) of gray scale values, normalize the values by multiplying  CDF values with the greatest gray scale level.
* Stretches the intensity values present in the image to the entire range of intensity values, thus increasing the contrast of the image.

**Sample Results:**

<table border="0">
 <tr>
    <td></td>
    <td><b style="font-size:15px"><p align="center">Image</b></td>
    <td><b style="font-size:15px"><p align="center">Histogram</b></td>
 </tr>
 <tr>
    <td><p align="center">Original</p></td>
    <td>
      <p align="center">
        <img width="400" src="Week1/Histogram Equalisation/8.png">
      </p>
    </td>
    <td>
      <p align="center">
        <img width="400" src="Week1/Histogram Equalisation/8-orig-hist.png">
      </p>
    </td>
 </tr>
 <tr>
    <td><p align="center">Enhanced</td>
    <td>
      <p align="center">
        <img width="400" src="Week1/Histogram Equalisation/8-after-manual-histequal.png">
      </p>
    </td>
    <td>
      <p align="center">
        <img width="400" src="Week1/Histogram Equalisation/8-equalized-hist.png">
      </p>
    </td>
 </tr>
</table>


### 2. Histogram Matching
* Extension of histogram equalization.
* This algorithm transforms a target image so that it’s histogram matches with the histogram of a given reference image.
* Firstly, histogram equalization is performed on both, the target and the reference image, which is then followed by the matching part.
* The target image histogram is manipulated such that it matches the histogram of the reference image.

**Sample Results:**

<table border="0">
 <tr>
    <td></td>
    <td><b style="font-size:15px"><p align="center">Image</b></td>
    <td><b style="font-size:15px"><p align="center">Histogram</b></td>
 </tr>
 <tr>
    <td><p align="center">Reference</p></td>
    <td>
      <p align="center">
        <img width="400" src="Week1/Histogram Matching/ref.jpeg">
      </p>
    </td>
    <td>
      <p align="center">
        <img width="400" src="Week1/Histogram Matching/ref-orig-hist.png">
      </p>
    </td>
 </tr>
 <tr>
    <td><p align="center">Target</td>
    <td>
      <p align="center">
        <img width="400" src="Week1/Histogram Matching/target.jpeg">
      </p>
    </td>
    <td>
      <p align="center">
        <img width="400" src="Week1/Histogram Matching/target-orig-hist.png">
      </p>
    </td>
 </tr>
 <tr>
    <td><p align="center">Target after Histogram Matching</td>
    <td>
      <p align="center">
        <img width="400" src="Week1/Histogram Matching/target-after-hist-match.jpeg">
      </p>
    </td>
    <td>
      <p align="center">
        <img width="400" src="Week1/Histogram Matching/target-match-hist.png">
      </p>
    </td>
 </tr>
</table>

### 3. Double Plateau Histogram Equalisation
* In the image histogram, there are certain grayscale values (bins) which have exceptionally high frequencies while some have very low.
* Thus, we select two threshold values of frequencies, and clip the bins according to these thresholds.
* The excess pixels in a high frequency bin are redistributed into the bins having low frequencies.

### 4. Top Hat Transform
* In digital image processing, the algorithm extracts minute elements and details from the images.
* Considering structural elements, the filter enhances bright  objects of interests in a dark background.
* Hence, it focuses on enhancing the light pixels in dark background.


## Acknowledgement

The code and documentation has been done by all 4 team members Aadesh Desai, Eshan Gujarathi, Saagar Parikh and Sanjay Venkitesh. We would like to thank Prof. Joycee Mekie (Assistant Professor, IIT Gandhinagar) and the Teaching Assistants for providing us with the necessary guidance during the course of the project.
