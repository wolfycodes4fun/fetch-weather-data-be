**Guide to deciphering the Comfort Index**  

For each city which you provide you're given with a comfort index which is calculated by taking into account the following parameters related to the weather:  
* Temperature
* Humidity
* Wind Speed

A **Multi-Criteria Weighted Scoring Algorithm** using **Piecewise Penalty Functions** is used to calculate this index. For each metric the corresponding weight is listed below. The score for each individual metric starts declining from 100 (perfect score) when the metric strays further away from the ideal range.  

| Metric | Weight | Range for Perfection | Unbearable L.B | Unbearable U.B |
| --- | --- | --- | --- | --- |
| Temperature | 0.5 | 21°C < T < 27°C | 10°C | 35°C |
| Humidity | 0.35 | 30% < H < 50% | 20% | 60%
| Wind Speed | 0.15 | 1.67 m/s < W < 3.06 m/s | 0 m/s | 6.67 m/s |

The penalties in the table above were calculated with the formula:  

penalty = 100 / unbearable (upper || lower) bound - (upper || lower) bound
