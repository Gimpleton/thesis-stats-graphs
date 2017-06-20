"# thesis-stats-graphs" 

1. In the Stats folder open "simulator_statitistics.py" and replace the two car ID's you are going to generate for in line 148 then run. This will generate a "ground_truth.csv" file in the Stats folder. Move that csv file to the "Graphs and Stats" folder. This file is needed to create the ground truth graph.

2. In Graph and stats folder open "Graphs.py". On line 185 you want to put your generated data array and on line 189 the seed array. Make sure to replace the first index of "gen_li" with the last index of "seed" and also remove car ID data from that index when you put it into "gen_li.

3. Run Graph.py and you should get a graph