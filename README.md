<h1 align="center">
  <br>
  <a href="https://notaroomba.dev"><img src="https://raw.githubusercontent.com/NotARoomba/Tamaki/main/assets/logo.png" alt="Tamaki" width="200"></a>
  <br>
  Tamaki
  <br>
</h1>

<h4 align="center">Project files for a custom Tamagotchi macropad.</h4>

<div align="center">

![Python](https://img.shields.io/badge/python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white)
![Fusion 360](https://img.shields.io/badge/fusion%20360-%23F78F1E.svg?style=for-the-badge&logo=autodesk&logoColor=white)
![KiCad](https://img.shields.io/badge/kicad-%2300578F.svg?style=for-the-badge&logo=kicad&logoColor=white)

</div>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#case-and-cad">Case & CAD</a> •
  <a href="#pcb">PCB</a> •
  <a href="#bom">BOM</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

![schematic](https://raw.githubusercontent.com/NotARoomba/Tamaki/main/assets/schematic.png)
![pcb](https://raw.githubusercontent.com/NotARoomba/Tamaki/main/assets/pcb.png)
![build](https://raw.githubusercontent.com/NotARoomba/Tamaki/main/assets/windowed.png)

## Key Features

- 4 Configurable Buttons (Cherry MX)
- 2 Rotary Encoders (EC11)
- 1 OLED 128x32 Display
- 1 WS2812B RGB LED
- USB Type-C
- KMK firmware
- OLED-powered Tamagotchi

## Case and CAD

The case includes:

- 3D printed parts: a base and a top cover
- 1 laser-cut acrylic cover to protect electronics
- Assembled with 4x M3 bolts and 4x M3 heatset inserts

Designed in Fusion 360.

<img src="assets/windowed.png" alt="CAD model" width="500"/>

## PCB

Designed in KiCad with a custom logo. Notable points:

- `MX_V2` switch footprints
- EC11 encoder footprints
- OLED header and single RGB LED support

<img src="assets/schematic.png" alt="Schematic" width="300"/> <img src="assets/pcb.png" alt="PCB" width="300"/>

## BOM

Everything you need to build Tamaki:

- 4x Cherry MX Switches
- 4x Keycaps (DSA or any profile)
- 4x M3x5x4 Heatset Inserts
- 4x M3 Bolts
- 1x WS2812B RGB LED
- 1x 128x32 0.91" OLED Display
- 2x EC11 Rotary Encoders
- 1x XIAO RP2040
- 1x Case (2 printed parts + 1 acrylic cover)

## Credits

This project uses:

- [KiCad](https://www.kicad.org/)
- [Python](https://www.python.org/)
- [Fusion 360](https://www.autodesk.com/products/fusion-360/overview)

## You may also like...

- [Niveles De Niveles](https://github.com/NotARoomba/NivelesDeNiveles) – Real-time flood alert app
- [ROCKETMEN](https://github.com/NotARoomba/ROCKETMEN) – Custom flight controller files

## License

MIT

---

> [notaroomba.dev](https://notaroomba.dev) &nbsp;&middot;&nbsp;
> GitHub [@NotARoomba](https://github.com/NotARoomba)
