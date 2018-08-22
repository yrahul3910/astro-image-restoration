## Point Spread Function

A PSF can be thought of as a mapping $\mathbb{R}^2 \mapsto \mathbb{R}$. That is, given a pixel position (x, y), it gives the response at that pixel position^[1]^. For an RGB image, it can be thought of as a vector-valued function.  

<u>Sources:</u>

[1] <http://www.cs.cmu.edu/afs/cs/academic/class/15462-s14/www/lec_slides/lec21.pdf> 

## An overview of the problem

Because of various factors including wrong positioning of the mirrors in a telescope, wind, and atmospheric turbulence (called *atmospheric seeing*), the images from telescopes are blurry. Taking the images again is not possible because certain events occur only once, and use of the telescope may be expensive^[2]^. Noise sources like wind cause *PSF anisotropy* (the PSF is different in different directions, i.e., there are visible “streak” patterns in the image^[1]^). The original images of stars (which are point sources) are circular, but the above factors cause blurring, “cut edges”, and non-circular shape^[2]^. The problem is to restore the original circular image of the star. 

<u>Sources:</u>

[1] <https://en.wikipedia.org/wiki/Anisotropy> 

[2] Discussion on Monday

## FITS Image Files^[1]^

The astronomical images are in the FITS format. They can be read using the tools IRAF and ds9. These are separate programs. IRAF requires the C Shell (csh). To run and view images, type: 

```shell
>> csh
$ cl
> cd <path to fits files directory>
> !ds9&
> display M13V20130911.fits 1
```

The constrast of the image can be changed by right-clicking anywhere in the image and dragging the mouse. To view a list of images, make a list file and view it in ds9: 

```
$ ls *.fits > list
$ cl
> imexamine @list 1
```

You can then view the other images in the list by hovering over the image and pressing n for next, and p for previous. Use *logout* to exit IRAF. 

<u>Sources:</u>

[1] Discussion on Monday

## Gravitational Lensing

As predicted by Einstein in his General Theory of Relativity, mass bends the space-time fabric. Because of this, light rays can be bent by massive objects such as galaxies or stars. This creates different images of a light source. It can cause the creation of “Einstein rings” as an image when a massive object such as a galaxy aligns with the light source. In *gravitational microlensing*, when a large object moves between the observer and the light source, the observed brightness of the source increases drastically, and then falls again. The brightness can be plotted over time to get a *light curve*, which appears as a Gaussian. Exoplanets can be detected using microlensing as well. When a planet and a large star come in between the observer and the light source, the light curve is a Gaussian with a small, observable distortion. This distortion indicates the presence of a planet, and is caused by gravitational lensing by the planet, whose effect is much weaker than that of the star^[1]^. However, microlensing is a rare phenomenon, and finding planets using microlensing is much rarer. Further, these events can only be observed once, after which there is no trace of the planet. Multiple visual examples can be found at [2]. A detailed study of planet detection using microlensing is found at [3].

<u>Sources:</u>

[1] <http://www.planetary.org/explore/space-topics/exoplanets/microlensing.html> 

[2] <https://en.wikipedia.org/wiki/Gravitational_lens> 

[3] https://arxiv.org/pdf/0902.1761.pdf

## Difference Image Analysis (DIA)

DIA performs image subtraction to detect objects. First, a model PSF, which is the best PSF we have, is found. This is subtracted from the other PSFs to get the difference image. The subtraction is a simple pixel-by-pixel subtraction^[1]^.

<u>Sources:</u> 

[1] Discussion on Monday

## Overview of the Photometric Method (DIA)^[1]^

Retrieving photometric information from images of crowded stellar fields is an important but difficult task. Overlapping stellar images cause the most serious complications. To tackle this problem, several groups now use image subtraction algorithms based on convolution kernels. To get the kernel, the Fast Fourier Transforms(FFT) of the two images to subtract are taken, and used in the equation 

 $$\text{Ker} = FFT^{-1} \left( \frac{FFT(PS_1)}{FFT(PS_2)} \right)$$

Recently an algorithm has been proposed in which the final difference is nearly optimal. The idea is to work on full pixel distribution of both images and do the calculation in real space:

$$\text{Image}(x, y) = \text{Ker}(x, y; u, v) \circledast \text{Ref}(u, v) + \text{Bkg}(x, y)$$

where Ref is a reference image, Ker is a convolution kernel, Bkg is a difference in background, and Image is a program image. We need to look at this in a least-squares sense to find the PSF-matching kernel. To do this, we minimize the squared difference between the images on both sides of the above equation, summed over all pixels.

<u>Sources:</u>

[1] https://arxiv.org/abs/astro-ph/0012143

## Denoising Images^[1]^

If $g \in \mathbb{R}^{n \times n}$ is the corrupted image and $f \in \mathbb{R}^{n \times n}$ is the original image, the random noise, which is independent of $f$ is given as

$$n = g - f$$

That is, noise added to the original images gives the corrupted images. Because $f$ is distributed at low frequency and $n$ is distributed at high frequency, a Discrete Wavelet Transform (DWT) *may* be helpful in denoising.

<u>Sources:</u>

[1] Sharjeel's Report

## Lensing Theory

If a gravitational lens is looked at as a physical lens, then we have the figure^[1]^:

<img src="/home/yrahul/Desktop/internship/img1.png" height="250px" width="auto" />

The deflection angle is given by, $\hat{a} = \frac{4GM}{c^2 b}$, where $b$ is an "impact parameter". The lens equation is

$$\begin{aligned} \boldsymbol \beta &= \boldsymbol \theta - \boldsymbol \alpha \\ \boldsymbol \alpha &= \frac{D_{LS}}{D_S}\hat{\boldsymbol \alpha} \end{aligned}$$

For a point mass, we have $b = \theta D_L$^[2]^

$$\begin{aligned} \boldsymbol \beta = \boldsymbol \theta - \frac{D_{LS}}{D_S}\frac{4GM}{c^2 D_L \theta} \end{aligned}$$

If the source is right behind the lens, then $\boldsymbol \beta = 0$, and we get the **Einstein radius**^[2]^:

$\theta_E = \sqrt{\frac{D_{LS}}{D_SD_L}\frac{4GM}{c^2}}$

Thus the lens equation is^[1]^,

$\boldsymbol \beta = \boldsymbol \theta - \theta_E^2 \frac{\boldsymbol \theta}{|\boldsymbol \theta|^2}$

* If $\boldsymbol \beta > \theta_E$ then the source is weakly lensed, and we get one weakly distorted image.
* If $\boldsymbol \beta < \theta_E$ then the source is strongly lensed and we get multiple images.

[3] is an additional resource on lensing.

<u>Sources:</u>

[1] https://www.cfa.harvard.edu/~dfabricant/huchra/ay202/lectures/lecture12.pdf

[2] https://www.astro.umd.edu/~miller/teaching/astr422/lecture13.pdf

[3] http://www.ita.uni-heidelberg.de/~massimo/sub/Lectures/gl_all.pdf

## Charge Coupled Devices (CCDs)

Read the sources below.

<u>Sources:</u>

[1] https://lco.global/spacebook/ccds/

[2] http://spiff.rit.edu/classes/phys445/lectures/ccd1/ccd1.html

## The KSB method

The forward process of image distortion^[1]^ is below:

![img2](/home/yrahul/Desktop/internship/img2.png)

There are two shearing parameters, $\gamma_1$ and $\gamma_2$, and a convergence parameter, $\kappa$. The **lensing Jacobian** is given by:

$A = \begin{bmatrix} 1 - \kappa - \gamma_1 & -\gamma_2 \\ -\gamma_2 & 1 - \kappa + \gamma_1 \end{bmatrix}$

The galactic ellipticity is given by^[1]^:

$e^{\text{obs}}=e^{\text{source}}+\gamma$

but, $<e^{\text{source}}> = 0$, so $\gamma = <e^{\text{obs}}>$.

<img src="/home/yrahul/Desktop/internship/img3.png" width="250px" height="auto" />

Due to lensing, a circle becomes an ellipse^[2]^

<img src="/home/yrahul/Desktop/internship/img4.png" height="300px" width="auto" />

### Centroids and Quadrupole Moments^[2]^

The first moment determines an object's centroid:

$\bar{x} = \int I(x, y) x \text{ } \mathrm{d}x \mathrm{d}y $

$\bar{y} = \int I(x, y) y \text{ } \mathrm{d}x \mathrm{d}y $

The second moment (quadrupole moments) determine shape:

$Q_{xx} = \int I(x, y) (x-\bar{x})^2\mathrm{d}x\mathrm{d}y$

$Q_{xy} = \int I(x, y) (x-\bar{x})(y-\bar{y}) \mathrm{d}x\mathrm{d}y$

$Q_{yy} = \int I(x, y) (y-\bar{y})^2\mathrm{d}x\mathrm{d}y$

<u>Sources:</u>

[1] http://www.astro.ipm.ir/ISGLT08/Lecture3.pdf

[2] http://www.roe.ac.uk/~heymans/KSBf90_for_DUEL/Download_Lecture_Notes_files/Lecture1_CH.pdf