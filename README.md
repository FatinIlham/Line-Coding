# Line-Coding
Line coding is the process of converting digital data to digital signals. By this technique we converts a sequence of bits to a digital signal.

Polar NRZ-L:
It is a Polar NRZ. Here two level of amplitude is used. The level of the amplitude determines the value of the bits. For example, binary 1 map to logic-level high and binary 0 map to logic- level low or vice versa.

![image](https://user-images.githubusercontent.com/61835955/178520643-81b7e67c-641d-4b3c-9599-a3e0a1e2363d.png = 500x)

Polar NRZ-I:
It is also a Polar NRZ. But here, two-level signal has a transition at a boundary. If the next bit that has going to be transmitted is a logical 1 then there is a transition, and if the next bit is logical 0, then there does not have any transition. So, the change or lack of change in polarity determines the value of a symbol.

![image](https://user-images.githubusercontent.com/61835955/178520843-d99fb305-97d7-490e-9060-42f81194d941.png)

Differential Manchester:
It is a combination of the RZ and NRZ-I schemes. There is always a transition at the middle of the bit but the bit values are determined at the beginning of the bit. It the next bit is 0, then there is a transition and if the next bit is 1, then there is no transition.

![image](https://user-images.githubusercontent.com/61835955/178521045-0b2e8051-581a-4ec5-9a19-f788f97e5496.png)


A-M-I:
It is a Bipolar scheme. Here three voltage level is used. Positive, Negative and Zero. A neutral Zero represents binary 0. And Binary 1 are represented by positive and negative voltages alternatingly.

![image](https://user-images.githubusercontent.com/61835955/178521270-9a776a72-5bf7-430a-ab72-11329e3bd6d6.png)

Pseudoternary:
It is also a Bipolar scheme. It is the opposite of AMI scheme. Here Bit 1 is represented by zero voltage and bit 0 is represented by positive and negative voltages alternatingly. 

![image](https://user-images.githubusercontent.com/61835955/178521422-2fad3403-d087-4ea9-a3c7-868885ad3d9e.png)

