# 109titration

Derivatives and preservatives.

Project for semester 2 of the Epitech Math module.

### Description

This project determines the concentration of benzoic acid in a soda using pH titration data. The program employs the derivative method to find the equivalence point by:

1. Calculating the derivative of the pH-titrant volume curve.
2. Identifying the maximum of the derivative to estimate the equivalence point.
3. Using linear interpolation to estimate second derivative values around the equivalence point.

## Getting Started

### Dependencies

- [Python3](https://python.org/)

### Installation

* Download/Clone the repository and enter its directory.
* Now you are ready to run the code.

## Usage

**Execution:** `./109titration file`

### Arguments
- **`file`**: CSV file containing titrant volume (ml) and pH values.

### Examples

To analyze data from `values.csv`:
```
$> ./109titration values.csv
Derivative:
2.0 ml -> 1.00
3.0 ml -> 0.73
5.0 ml -> 0.20
6.0 ml -> 0.80
7.0 ml -> 1.53
7.5 ml -> 2.00
8.0 ml -> 2.27
9.0 ml -> 1.61
12.0 ml -> 0.22
14.0 ml -> 0.07
16.0 ml -> 0.06
Equivalence point at 8.0 ml
Second derivative:
3.0 ml -> -0.27
5.0 ml -> 0.31
6.0 ml -> 0.67
7.0 ml -> 0.87
7.5 ml -> 0.73
8.0 ml -> 0.14
8.1 ml -> 0.06
8.2 ml -> -0.01
8.3 ml -> -0.09
8.4 ml -> -0.16
8.5 ml -> -0.24
8.6 ml -> -0.31
8.7 ml -> -0.39
8.8 ml -> -0.46
8.9 ml -> -0.53
9.0 ml -> -0.61
Equivalence point at 8.2 ml
```

## Acknowledgments

* [Epitech](https://www.epitech.eu/)

## Authors

* **Daniel Sanchez** ([GitHub](https://github.com/angsanch) / [LinkedIn](https://www.linkedin.com/in/angeldanielsanchez/))
* **Xinru Xu** ([GitHub](https://github.com/Exinru) / [LinkedIn](https://www.linkedin.com/in/xinru-xu/))

## License

This project is licensed under the GNU Public License version 3.0 - see the [LICENSE](LICENSE) file for details.
