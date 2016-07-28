#NVIDIA Shield Android TV - Reverse Engineering

![shield_mainboard_connector](https://senselessdev.github.io/nvidia-shield-tv-pinout/shield_mainboard_connector.svg)

![shield_ioboard_bottom](https://senselessdev.github.io/nvidia-shield-tv-pinout/shield_ioboard_bottom.svg)

![shield_ioboard_top](https://senselessdev.github.io/nvidia-shield-tv-pinout/shield_ioboard_top.svg)

## Sorted by J501 pin number

| J501 pin | description                                                 | mainboard pin |
| -------- | ----------------------------------------------------------- | ------------- |
| 1        | GND                                                         | R7            |
| 3        | RTL8153 USB D+ (Pin 23)                                     | Q7            |
| 5        | RTL8153 USB D- (Pin 22)                                     | P7            |
| 7        | GND                                                         | X11           |
| 9        | USB Jack J6 SSRX- (Pin 8)                                   | W11           |
| 11       | USB Jack J6 SSRX+ (Pin 9)                                   | W12           |
| 13       | GND                                                         | X12           |
| 15       | USB Jack J5 D- (Pin 2)                                      | X13           |
| 17       | USB Jack J5 D+ (Pin 3)                                      | W13           |
| 19       | GND                                                         | S12           |
| 21       | USB Jack J5 SSRX- (Pin 8)                                   | T11           |
| 23       | USB Jack J5 SSRX+ (Pin 9)                                   | T12           |
| 25       | GND                                                         | V13           |
| 27       | USB Jack J7 OTG D- (Pin 2)                                  | U12           |
| 29       | USB Jack J7 OTG D+ (Pin 3)                                  | U13           |
| 31       | GND                                                         | Q6            |
| 33       | HDMI Jack J3 Data 0 + (Pin 7)                               | Q5            |
| 35       | HDMI Jack J3 Data 0 - (Pin 9)                               | Q4            |
| 37       | GND                                                         | P4            |
| 39       | HDMI Jack J3 Data 1 + (Pin 4)                               | P5            |
| 41       | HDMI Jack J3 Data 1 - (Pin 6)                               | O5            |
| 43       | GND                                                         | P6            |
| 45       | HDMI Jack J3 Data 2 + (Pin 1)                               | O6            |
| 47       | HDMI Jack J3 Data 2 - (Pin 3)                               | N6            |
| 49       | GND                                                         | N5            |
| 51       | HDMI Jack J3 Clock + (Pin 10)                               | O4            |
| 53       | HDMI Jack J3 Clock - (Pin 12)                               | N4            |
| 55       | GND                                                         | U5            |
| 57       | Voltage ?                                                   | T5            |
| 59       | Voltage ?                                                   | T6            |
| 61       | Voltage ?                                                   | V6            |
| 63       | -> Q7 (Pin 2); Q7 (Pin 3) -> J502 (Pin 8) (Levelshifting ?) | W10           |
| 65       | -> Q6 (Pin 2); Q6 (Pin 3) -> J502 (Pin 4) (Levelshifting ?) | U6            |
| 67       | U4 (Pin 3 and 4) (High Side USB Current Switch?)            | W9            |
| 69       | U5 (Pin 3 and 4) (High Side USB Current Switch?)            | W8            |
| 71       | Q4 (Pin 1) (Levelshifting ?)                                | X8            |
| 73       | Q8 (unpopulated) (Levelshifting ?)                          | X9            |
| 75       | GND                                                         | N8            |
| 77       | USB Jack J6 D- (Pin 2)                                      | N7            |
| 79       | USB Jack J6 D+ (Pin 3)                                      | O7            |

| J501 pin | description                                                 | mainboard pin |
| -------- | ----------------------------------------------------------- | ------------- |
| 2        | GND                                                         | X5            |
| 4        | microSD slot RSV/DAT1 (Pin 8)                               | W4            |
| 6        | microSD slot MISO/DAT0 (Pin 7)                              | X4            |
| 8        | microSD slot CLK (Pin 5)                                    | W5            |
| 10       | microSD slot MOSI/CMD (Pin 3)                               | X6            |
| 12       | microSD slot CS/DAT3 (Pin 2)                                | V5            |
| 14       | microSD slot RSV/DAT2 (Pin 1)                               | W6            |
| 16       | D502 (open ?)                                               | V7            |
| 18       | GND                                                         | V4            |
| 20       | -> Q5 (Pin 2); Q5 (Pin 3) -> J502 (Pin 7) (Levelshifting ?) | V11           |
| 22       | U6 Pin 1 (Function ?)                                       | V10           |
| 24       | J502 (Pin 2)                                                | X10           |
| 26       | J7 OTG ID (Pin 4, through diode)                            | U10           |
| 28       | HDMI Jack J3 CEC (Pin 13)                                   | S6            |
| 30       | HDMI Jack J3 Hot Plug Detect (Pin 19)                       | S5            |
| 32       | HDMI Jack J3 DDC Data (Pin 16)                              | R6            |
| 34       | HDMI Jack J3 DDC Clock (Pin 15)                             | R5            |
| 36       | Power Button J502 (Pin 6)                                   | S11           |
| 38       | ?                                                           | R12           |
| 40       | ?                                                           | Q12           |
| 42       | ?                                                           | P13           |
| 44       | GND                                                         | U11           |
| 46       | SATA Jack J504 (Pin 16, AC coupled)                         | O11           |
| 48       | SATA Jack J504 (Pin 15, AC coupled)                         | O12           |
| 50       | GND                                                         | R11           |
| 52       | SATA Jack J504 (Pin 19, AC coupled)                         | N12           |
| 54       | SATA Jack J504 (Pin 18, AC coupled)                         | N13           |
| 56       | GND                                                         | O13           |
| 58       | USB Jack J6 SSTX+ (Pin 6, AC coupled)                       | P11           |
| 60       | USB Jack J6 SSTX- (Pin 5, AC coupled)                       | P10           |
| 62       | GND                                                         | Q11           |
| 64       | USB Jack J5 SSTX+ (Pin 6, AC coupled)                       | N10           |
| 66       | USB Jack J5 SSTX- (Pin 5, AC coupled)                       | O10           |
| 68       | GND                                                         | N11           |
| 70       | RTL8153 USB SSRX+ (Pin 14)                                  | N9            |
| 72       | RTL8153 USB SSRX- (Pin 15)                                  | O9            |
| 74       | GND                                                         | O8            |
| 76       | RTL8153 USB SSTX- (Pin 19)                                  | P8            |
| 78       | RTL8153 USB SSTX+ (Pin 18)                                  | Q8            |
| 80       | GND                                                         | P9            |

## Sorted by mainboard pad number

| marking | meaning                                                |
| ------- | ------------------------------------------------------ |
| *x*     | non existing pads on mainboard                         |
| *u*     | no connection on flat flex cable (**u**nconnected)     |
| *o*     | pad on mainboard but no spring on connector (**o**pen) |
| *g*     | **g**round pads (more on mainboard than pins on J501)  |


|        |  N  |  O  |  P  |  Q  |  R  |  S  |  T  |  U  |  V  |  W  |  X  |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **13** | 54  | *g* | 42  | *u* | *x* | *x* | *x* | 29  | *g* | 17  | 15  |
| **12** | 52  | 48  | *u* | 40  | 38  | *g* | 23  | 27  | *g* | 11  | *g* |
| **11** | *g* | 46  | 58  | *g* | *g* | 36  | 21  | *g* | 20  |  9  | *g* |
| **10** | 64  | 66  | 60  | *u* | *o* | *x* | *x* | 26  | 22  | 63  | 24  |
| **9**  | 70  | 72  | *g* | *u* | *x* | *x* | *x* | *x* | *g* | 67  | 73  |
| **8**  | *g* | *g* | 76  | 78  | *x* | *x* | *x* | *x* | *g* | 69  | 71  |
| **7**  | 77  | 79  |  5  |  3  | *g* | *x* | *x* | *x* | 16  | *g* | *g* |
| **6**  | 47  | 45  | *g* | *g* | 32  | 28  | 59  | 65  | 61  | 14  | 10  |
| **5**  | *g* | 41  | 39  | 33  | 34  | 30  | 57  | *g* | 12  |  8  | *g* |
| **4**  | 53  | 51  | *g* | 35  | *x* | *x* | *x* | *u* | *g* |  4  |  6  |
