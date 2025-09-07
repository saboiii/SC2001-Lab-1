# SC2001 Lab 1: Hybrid Mergesort Algorithm

This project implements and analyzes a hybrid sorting algorithm that combines Mergesort with Insertion Sort for improved efficiency on small subarrays.

## Overview

The hybrid algorithm uses a threshold value `S` to determine when to switch from Mergesort to Insertion Sort. When the size of a subarray becomes ≤ S, the algorithm switches to Insertion Sort, which is more efficient for small datasets due to lower overhead.

## Files Structure

- `algorithm.py` - Main implementation
- `final-analysis.py` - Perform anallysis
- `requirements.txt` - Python dependencies
- `README.md` - This documentation file
