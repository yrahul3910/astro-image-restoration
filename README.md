# README
This readme provides an explanation of each file. All code files are properly named and documented, so this will not explain the details of the code.

* `reportSharjeel.odt`: The report by the previous student, Sharjeel.
* `ksb orig paper.pdf`: The original paper on the KSB reconstruction method.
* `internship_Report.pdf`: A report on the problem statement and some background information. This is a useful starting point, but a lot of the information is from Wikipedia/other sources.
* `harvard lensing notes.pdf`: Harvard notes on gravitational lensing. The initial slides give a helpful introduction to the concept.
* `Wozniak_DIA.pdf`: A DIA (Difference Image Analysis) method proposed by Wozniak. Not very useful, since to compute the PSF, I instead used the library that used a different algorithm ultimately.
* `Noise2Noise - Learning Image Restoration without Clean Data.pdf`: An interesting relevant paper, but not used in this project.
* `Lecture3.pdf`: Lecture slides on the KSB method. Useful because it provides information about how images get corrupted in the first place.
* `Lecture1_CH.pdf`: Another nice introductory lecture slides by the same professor as above. Contains some useful diagrams. I've incorporated these into my 'current understanding' notes.
* `Image Restoration in Astronomy A Bayesian Perspective.pdf`: An interesting paper, but I haven't gone through the details.
* `Astronomical Image Reconstruction using CNNs.pdf`: The basis for the model implemented in the 'OtherCNN' folder.
* `current understanding`: A collective summary of an introduction to the problem statement along with references where the information was taken.
* `OtherCNN`: The implementation for the other neural network proposed (3-layer). Contains the data, code to generate the noisy dataset, and the model.
* `IRCNN_impl`: Full implementation with checkpoints of trained models of the Image Restoration CNN (IRCNN) model.
* `GoodFrames`: Some non-corrupted FITS images. Useful for reference and for understanding the format.
* `BadFrames`: Some corrupted FITS images. Useful for reference and to understand what kind of corruptions may occur.
* `ASI conference`: Abstract for the conference in Kolkatta.

## Some Observations
It appears that the 3-layer neural network for some reason is pretty bad at what it aims to do. Even with the paper author's implementation, as used in `OtherCNN/PaperPretrained/` and the `Paper Pretrained Model (M31)` notebook, it does a bad job at maintaining the original image.

The 6-layer IRCNN, on the other hand, does considerably better. Even though it was trained on Rayleigh noise that was found by subtracting PNG images, it worked    remarkably well on both test (astronomical) PNG data as well as FITS data. However, it appears that there are two "kinds" of these FITS files, as viewed in `ds9`. One type is viewed by setting the scale to "histogram", and the other is viewed by setting the scale to "z-scale" (the last option). Clearly, from the `IRCNN_impl/Testing trained CNN model.ipynb` notebook, the network does well on the first type--the difference between the images is remarkably low, and the differences between the maximum and minimum intensity values before and after running through the CNN is reasonably small. However, with the other type, as seen in the same notebook (the last section), it does not perform well. This is seen with the help of the "BadM13..." FITS file, about 17 MB, which is this kind. While the min values seem large, it should be noted that the left side of the image seems to be vastly different, which may be the cause. The center of the image also looks rather distorted. Perhaps this is because of the low number of epochs the model was trained on (16).

Overall, the IRCNN model seems promising indeed, and with the right kind of care in training, it could be incredibly effective for the task.
