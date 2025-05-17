# Phase Interferometer
### Max Kendall

At a high level, this is a system that uses 3 antennas (elements) to esitmate the approximate direction of an incoming radio signal. This means that you're able to get the location of an object in a protocol-agnostic manner! The vision is that this is mostly portable (aside from the antennas) and can be whipped out anywhere to get a quick bearing.

The hardware contains 3 RF frontends, including 1 amplifier, 1 mixer, and 1 filter for each element. It uses a mixer to be able to directly feed the signal into the onboard RP2040 microcontroller. It then would perform a phase analysis to determine which signals reach the pins first.
Since we're dealing with a phased-array, we need to perform length tuning to make sure all the tracks are electrically the same length. KiCAD has a great built-in tool for this!

Here's the features/specs:
- RP2040 MCU
- 3x 433 MHz frontends
- USB-C
- 4-layer board
- via fencing/stitching
- broken-out gpio headers for all free pins
- LO for all mixers

## Super cool pics:
![](https://hc-cdn.hel1.your-objectstorage.com/s/v3/06e0e1aaaa2490bb132aaf519ddf6046336ec269_image.png)
![](https://hc-cdn.hel1.your-objectstorage.com/s/v3/63ea85745522ec6cce893365a249b4e1da2d8166_image.png)

Main repository can be found [here](https://github.com/maxsrobotics/phase-interferometer).