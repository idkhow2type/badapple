# Bad Apple, but it's slimes in Minecraft

`//TODO: add thumbnail`

A Python program that creates a Minecraft datapack that plays Bad Apple in real-time using the slime (and magma cube if you choose) mobs in Minecraft with the Quad Tree algorithm

To use this project, go into `config.json` and change the settings

-   `"width"`, `"height"` and `"fps"`: quite literal

-   `"cutoff"`: the maximum number of frames stored in a `.mcfunction` file. Shouldn't be set too big or the file won't be loaded into the game

-   `"magma"`: whether to display black regions as magma cubes instead of ignoring them

Go in the outer folder and run

```
py toframe.py mcslime
```

Go back in this folder and run

```
py main.py
```

and wait for it to finish
Then, copy the `badappleslime` folder into the `datapacks` folder of your Minecraft world
Open the world, run the command

```mcfunction
/execute positioned <x> <y> <z> run function badappleslime:play
```

with `<x>`, `<y>`, and `<z>` as the coordinates of the top left corner of the video
