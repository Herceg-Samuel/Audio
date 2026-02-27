## Introduction to Audio Data

# Sound

Sound is continuous in nature.
It follows a wave structure.

# Signals

The electrical signal is then digitized by an Analog-to-Digital Converter to get the digital representation through sampling.

# Representation

The analog signal is first captured by a microphone, which converts the sound waves into an electrical signal.

The electrical signal is then digitized by an Analog-to-Digital Converter to get the digital representation through sampling.

# File Formats

File formats such as:
.wav (Waveform Audio File),
.flac (Free Lossless Audio Codec)
and .mp3 (MPEG-1 Audio Layer 3).

# Sampling

Sampling is the process of measuring the value of a continuous signal at fixed time steps.
The sampled waveform is discrete.(Hz)

The choice of sampling rate primarily determines the highest frequency that can be captured from the signal. ==> Nyquist which is a half the sampling rate(8KHz humans)

Resampling is the process of making the sampling rates match

# Amplitude and bit depth

Amplitude -> sound pressure level at any given instant(decibels(dB))
Perceived as loudness.

Bit depth -> precision of amplitude
16 and 24 bits.

32-bit audio stores the samples as floating-point values, whereas 16-bit and 24-bit audio use integer samples.

human hearing is logarithmic in nature — our ears are more sensitive to small fluctuations in quiet sounds than in loud sounds — the loudness of a sound is easier to interpret if the amplitudes are in decibels, which are also logarithmic.

# The frequency spectrum/ domain

The spectrum is computed using the discrete Fourier transform or DFT. It describes the individual frequencies that make up the signal and how strong they are.

# spectrogram.

A spectrogram plots the frequency content of an audio signal as it changes over time.
