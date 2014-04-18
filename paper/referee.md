#Comments on the manuscript

Impact of gas bulk rotation on the Lyman-alpha line
In this study, the authors investigate the effect of bulk rotation on the transfer of Lyman-alpha
photons through a spherical cloud. I recommand the publication of the article after some changes.
To my mind, the main result of this study is that rotation, although breaking the spherical symmetry
of the problem, does not create any anistropy in the lya properties of rotating clouds, at least in the
range of investigated parameters and for spherical distributions of sources.

#Global comments:

##Variation with viewing angle

The problematic of anisotropy is only studied from Sect3.4, the former sections consider global quantities
(spectral shapes, escape fractions, etc...). This is ok only if there is NO anisotropy induced by rotation,
which is not obvious, a priori. You should make it clear from the beginning, telling that you will
investigate anisotropy at the end of the paper only, because you checked that lya properties are isotropic,
at least in the range of parameters that you investigated so far.

As explained in sect 3.4, rotation kills the spherical symmetry of your problem, and the rotation axis
defines a preferential direction. We could expect some variation of the emerging flux, the lyman-alpha
escape fraction, and the spectral shape, with viewing angle. From Fig8, it seems that the flux is the same
in all directions for spherical distributions of sources. This important result is not enough emphasized.

Do you see any difference in the spectral shape with viewing angle ? To illustrate this point, it would
be interesting to build a 2D plot as you did on Fig 5, but replace Nb scat in ordinates by the viewing
angle μ. We could immediatly see if there is an evolution of the shape with viewing angle or not. If you
find NO evolution of the Lya shape with viewing angle, I think that it is an interesting counter-intuitiv
result, that you should advertise more.

What about the variation of lya escape fraction with viewing angle ?
I propose that in the beginning of Sect.3 Results, you first emphasize that, maybe counter-intuitively,
you did not find any variation of the Lya properties with viewing angle, so you will present first angleaverage
lya properties, and you will come back to the anisotropy problematic only at the end on the
paper.

######(JNGC)

##Intrinsic spectrum:

You discuss the line broadening of the profile by rotation, on Fig2, and the transition from double-peaked
to single-peaked profiles on Fig3 when Vmax 1/2 FWHM. Do you have an idea of the influence of the
FWHM of the intrinsic lya line on your results ? You use monochromatic intrinsic spectrum. How would
it change your results if you consider more realistic gaussian shape, for example with FWHM ∼ Vmax ?

######(JEFR)

* ##Remark on the form
At several places, you make some conjectures in the text (for example: in this case, the average number
of scatterings to escape should remain close to constant as the rotational velocity increases), whereas
the answer is after, on a following plot. Please reformulate : at the location of the demonstrating plot,
explain how it shows/demonstrates your point (the existence of a photosphere should be mentionned
during the discussion of Fig4, not before).

###### (JNGC)

* ##Outflow+rotation ?
So far, the model only includes rotation. However, most observed Lya spectra from LAEs, or even local
galaxies, seem to be asymetric towards the red wavelengths, interpreted as a sign for outflows in these
systems, often corroborated by others observables. Did you investigate how the rotation would modify
the spectra emerging from expanding clouds?

###### We agree that outflows are an important aspect to explain
       observed spectra. However we did not investigate outflows and
       rotation. Actually, this is subject of ongoing investigation (JNGC) 



* #Details:

##Introduction
With Orsi et al 2012, please cite also Garel et al 2012.
With Zheng&Wallace 2013, please cite also Behrens et al 2014.

######(Done)

##Fig1
I guess that the spectra presented in Fig1 are integrated over all directions, right ? You should describe
explicitly how you build them. You could skip the x notation in absciss, as it is not used in the discussion,
whereas the velocity is used to compare to FWHM, on Fig2.

#######(Done)

##Fig2
Can you explain how you measure the FWHM of a double-peaked profile ?
Do you fit it with a gaussian ?

######(JNGC)

##Fig3
Do you have an idea why the (central source, intermediate optical depth) case with Vmax=300 has a
single plateau instead of 2 peaks ? Do you find this with the two codes ?

######(JEFR)

##Fig4 and 6
This is a surprising result that the number of scatterings (escape fraction) stays constant as the rotation
velocity increases, for a central source, whereas the global spectral shape is altered. Did you try with
higher/extreme values of Vmax (=1000 km/s, even if not physically motivated) ? Do you believe that the
number of scatterings decreases with very high values, or that it is independant of the rotation velocity
? Is the escape fraction from a dusty rotating cloud with central source independant of the rotation
velocity ?


##Fig5
This is a very nice figure ! Looking at the top right panel, with its “photosphere”, I’m surprised that
the distribution of Nscatt is bipolar, I would have expected a smooth transition between the 2 regimes.
Do you have a physical explanation why photons escape after either (less than 10) or (more than 1000)
scatterings, and none escape with 100 scatt ?
To test the ’photosphere’ assumption, you could also do the radiation transfer in a cloud with the
distribution of sources only in an inner sphere, and another experienment with sources only in an outer
shell. If I understood corectly, you would expect thant the bottom spot on the top right panel is made
of photons from the outer shell, and the uppper spot from photons emitted inside the cloud.

######(JNGC)/(JEFR)

##End of paragraph 3.3
One sentence is not clear : we see that the escape fraction does not increase significantly from τ = 105 to
τ = 106. This counter-intuitiv result.... It sounds like you were expecting a strong increase... A decrease
is expected from τ = 105 to τ = 106, not an increase, but indeed on the graphe we can see an unexpected
(small) increase. I do not understand the explanation for this behaviour.

######(Mark)

##Fig8
Referred to as Figure 7 in the text (paragraph 3.4).
To my mind, this figure illustrates the main result of your study, it has to be more demonstrative.
On this figure, the numerical noise seems very big compare to the small number of bins, bigger than
on the spectra from Fig1, how is it possible ? Could you re-do this figure with more photons, maybe
with more bins ? Could you plot an histogram instead of broken lines, to ease the reading ? In the text,
you write anisotropy induced by rotation is at the 3% level, how do to estimate this number? I think
that the noise is at 3% level, and the distribution is compatible with ’flat’.
In the corresponding text, you first say that F(μ) does not depend on Vmax. Again, if real, this is an
important result, that you must advertise more. Please show it on this Fig, by comparing F(μ) without
rotation (in red, for example) to the other distributions that you get with different values of Vmax.
Then, you mention that for high optical depth values, F(μ) (not the variations of μ) can vary up to
15%. First, what do you call high optical depth ? your highest setup is τ = 107, not extremely high for
lyman alpha ”standards’, corresponding to NHI ∼ 1020 cm−2. So, if you see a trend with optical depth,
I encourage you to check higher optical depth regimes, corresponding better to galaxy scales. If you
can probe that anisotropy induced by rotation is rising with optical depth, this would be an interesting
result.  
If higher optical depth regimes lead to anisotropic escape, could you check the effet of anisotropy on
the lya spectral shape ?

######(JNGC)/(JEFR)

##Paragraph 3.4
You discuss in the same paragraph two very different things. You should not mix a very interesting study
of the (an-)isotropy of emerging radiation after transfer through an axi-symetrical configuration, with a
fortuitous discovery of peculiar spectral shapes emerging after transfer through the same configuration,
but from a peculiar, asymetric distribution of sources. Please, separate the two discussions in two
paragraphs, one related to Fig8, modified as proposed above, the other one related to Figs 7, 9 and 10.

######(JNGC)

##Fig 7, Fig9 and Fig10
In general, the last part of the paper, about triple peaks and a
comparison of these with observations, is less convincing. What is the
physical motivation for the peculiar geometry described on Fig7, by 2
off-centered spheres emitting Lya photons? 

######(The main motivation for this study was to explore a different
      source of anisotropy in the lya emission. We decided to report
      on the triple peaked emission as it is also a consequence of
      rotation.)


In order to test if the assymetry created by non-spherical distribution of sources is higher than the
anisotropy created by rotation, could you check F(μ) for this configuration in the static case (Vmax =
0), with F(μ) when Vmax increases. So, could you do the same as Fig8, for this strange configuration
of sources ?

######(JNGC)

Could you also show that the spectral shape of this configuration with (Vmax=0, τH = 105 , C=
+0.75) is not triple-peaked ?
######(JNGC)

You could skip the x notation in absciss, as it is not used in the discussion, whereas the peaks
separation, in velocity, is used to compare to instrumental resolution.


About the detectability of triple peaks, some instruments have much higher spectral resolution than
the one you mentionned (VLT-XSHOOTER, HST-COS for example). You should clearly say in this part
that you want to compare your spectra with peculiar lya spectra reported recently from Kulas+2012,
Yamada+2012, which are mid-resolution spectra. It is very easy to convolve your spectra with a gaussian
to mimic instrumental effect. You can then test directly if the triple peaks would be recovered, or what
is the spectral resolution needed to recover the peaks separation.

######(We have veryfied that a spectral resolution of 200km/s is
	  enough to resolve the triple peaks only in the case of our
	  most massive object (tau=10^7) and high rotational
	  velocities (200km/s).

	  
But you should also consider the higher resolution Chonis+2013 spectra. They claim that they
may observe a triple peaked spectrum. However the peaks separtion is so big (> 1000 km/s) that it
may belong to different interacting objects. In general, the maximum separation of the peaks in your
configuration is < 300 km/s (read on Fig 10), which is much less than the peaks separation reported
by Kulas+2012 (for their single triple peaked object,> 500 km/s, read from their Fig5). This may also
come from the optical depth of your medium which not high enough ?

######(We now mention Chonis+2013 in this Section. Concerning
      Kulas+2012 their spectra in Fig5 are redshifted by a factor of
      4.0, so in reality the separation of their peaks is on the order
      of 150km/s, a shift that can be expected from our models.) 


* #Conclusions
Again, after a careful checking of the influence of optical depth on the anisotropy induced by rotation,
I would put this result first : The spatial anisotropy induced by rotation in the emission in usually
below 10%. Because it justifies why you can consider/discuss angle-average effects of rotation on the lya
properties of your spherical clouds.

######(Done)
