**Guide to deciphering the Comfort Index**  

For each city which you provide you're given with a comfort index which is calculated by taking into account the following parameters related to the weather:  
* Temperature
* Humidity
* Wind Speed
* Cloudiness
* Pressure
* Visibility

A **Multi-Criteria Weighted Scoring Algorithm** using **Piecewise Penalty Functions** is used to calculate this index. For each metric the corresponding weight is listed below.  

| Metric | Weight | Range for Perfection |
| --- | --- | --- |
| Temperature | 0.35 | 20°C < T < 24°C |
| Humidity | 0.25 | 30% < H < 50% |
| Wind Speed | 0.15 | 1.5 m/s < W < 4.0 m/s |
| Cloudiness | 0.10 | 20% < C < 40% |
| Pressure | 0.08 | 1010hPa < P < 1016hPa |
| Visibility | 0.07 | V >= 10,000m |

The penalty for each unit over or under the ideal range for each metric is defined as follows:  

<table>
    <thead>
        <tr>
            <th>Metric</th>
            <th colspan="2">Unbearbale bounds</th>
            <th>Unbearable upper bound</th>
            <th>Unbearable lower bound</th>
            <th>Penalty</th>
        </tr>
    </thead>
    <tbody>
    </tbody>
</table>

The penalties in the table above were calculated with the formula:  

penalty = 100 / unbearable (upper || lower) bound - (upper || lower) bound
<table>
  <thead>
    <tr>
      <th colspan="2">Main Category (Spans 2 Columns)</th>
      <th>Details</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Item A</td>
      <td>Item B</td>
      <td>Description for items A and B</td>
    </tr>
    <tr>
      <td colspan="2" align="center"><b>All Systems Operational (Spans 2 Columns)</b></td>
      <td>Active</td>
    </tr>
  </tbody>
</table>