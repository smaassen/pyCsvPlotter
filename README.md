# pyCsvPlotter

A simple plotter in python for `.csv` files. 

### Usage

Run the python file in console specifying the file location

```
python plotter.py <fileName>.csv
```

It is possible to assign an axis to plot the other items against.

```
python plotter.py <fileName>.csv axis=<variable>
```

You can also specify variables that should be plotted while neglecting the others

```
python plotter.py <fileName>.csv <variable1> <variable2>
```

### Example use

An example use for the plotter with the provided `test.csv`file would look like 

```
python plotter.py test.csv axis=t x y 
```

