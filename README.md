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
      <th>Category</th>
      <th>Feature</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <!-- Merged Row across 2 rows -->
    <tr>
      <td rowspan="2">Core Engine</td>
      <td>Speed</td>
      <td>Optimized for fast execution.</td>
    </tr>
    <tr>
      <td>Memory</td>
      <td>Low footprint usage.</td>
    </tr>
    <!-- Merged Column across 2 columns -->
    <tr>
      <td>Extensions</td>
      <td colspan="2">Supported via plugins and custom hooks.</td>
    </tr>
  </tbody>
</table>