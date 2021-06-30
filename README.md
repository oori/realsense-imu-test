Caprinae IMU test
=================

*23/may/2021*

# CSV recordings notes
 - There's always little trash at start and end of each file
 - Each step is 60cm (`2B`) or 30cm (`1B`).
 - Same path always. 1B have 18 steps, 2B have 9.
 - Starting foot is RIGHT. Filenames with `L` suffix (*eg. 30L.csv*) means starting with LEFT foot.

# Recorded gait sequence
    + (trash ~0.5s) turn from laptop to start position
    + 9/18 steps
    + full stop
    + 180 turn
    + full stop
    + 9/18 steps
    + full stop.
    + (trash ~0.5s) turn toward laptop to stop check recording

# CSV Catalog
`30` --> 30, 30L, 31...

Barefoot:
`30`: 2B - normal gait
`40`: 1B - normal gait

Shoes:
`50`: 2B - normal gait
`60`: 1B - normal gait

`70`: 2B - strong steps
`80`: 1B - strong steps, lean forward

`90`: 2B - slow gait, lean backwards
`100`: 1B - slow gait, lean backwards

`110`: 2B - fast gait
`120`: 1B - fast gait

