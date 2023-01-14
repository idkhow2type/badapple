>-[-[-<]>>+<]>- set 32
[>+>+<<-] duplicate 32
>>+++ set 35
>++++++++++
> init print flag
>> init temp0 and temp1
>- set anchor
! input data here: 

+[-<+]-
copy width and height
  >[->>+>+<<<]
  >>>[-<<<+>>>]
  <<[->>+>+<<<]
  >>>[-<<<+>>>]

+[-
  set print flag
    +[-[[-<<+>>]<<+>>-<]>+]-<<[->>+<<]>>-[
      -
      +[-<+]-
      <<<+
      >>
    ]>
  +[-<+]-
  >>>>>+[-[[-<<+>>]<<+>>-<]>+]-<<[->>+<<]>>+ bodge offset fix
  +[-<+]-
  >>>>[>
    +[-[[-<<+>>]<<+>>-<]>+]-<<[->>+<<]>> go to image data
    - subtract from image data

    flip print flag if image data == 0
      temp0< [-]+
      temp1< [-]
      x>> [
        code1 (none)
        temp0< -
        x> [temp1<< +x>> -]
      ]
      temp1<< [x>> +temp1<< -]
      temp0> [
        code2
          +[-<+]-
          <<<
          x = !x
            temp0> [-]
            x< -
            [temp0> -x< -]
            temp0> [x< +temp0> -]
          go to temp0
          >>>>>>>
          +[-[[-<<+>>]<<+>>-<]>+]-<<[->>+<<]>>
      temp0-]
    +[-<+]-
    display pixel
      temp0<< [-]+
      temp1> [-]
      x<< [
      code1
        <<<.
      x>>> >-]>
      [<
      code2
        <<.
      x>> >->]<<

    line logic
      +[->+]->>>-
      temp0>> [-]+
      temp1> [-]
      x<<< [
        code1 (none)
        temp0>> -
        x<< [temp1>>> +x<<< -]
      ]
      temp1>>> [x<<< +temp1>>> -]
      temp0< [
        code2
          copy width
            <<<<[->>+>>>>+<<<<<<]
            >>>>>>[-<<<<<<+>>>>>>]
          subtract height
            <<<-
          print \n
            <<<<<<<<.
      temp0>>>>>>>>> -]
      +[-<+]->>>>
  ]
  <<[->>+>+<<<]
  >>>[-<<<+>>>]
  <<<<<<<<- reset print flag
  >>>[>]+[-[[-<<+>>]<<+>>-<]>+]-<<[->>+<<]>>- bodge offset fix p2
  ,[-] pause after frame
  check for end of input
    >+
    temp0< [-]+
    temp1<< [-]
    x>>> [
      code1 -
      temp0< -
    x> [temp1<< +x>> -]
    ]
    temp1<< [x>> +temp1<< -]
    temp0> [
      code2 <-
    temp0> -]
    <
+]