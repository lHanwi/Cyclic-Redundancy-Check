# Cyclic Redundancy Check

## Project Description

This project implements Ethernet CRC-32 generation and verification in Python.

The program simulates the Frame Check Sequence (FCS) mechanism used in Ethernet frames to detect transmission errors.

Given the frame fields:

- Destination MAC Address
- Source MAC Address
- EtherType
- Payload

the program can:

1. Generate the CRC-32 value for an outgoing frame.
2. Append the CRC to the frame.
3. Verify the CRC of a received frame.
4. Determine whether the received frame is valid or corrupted.

---

## CRC Generator Polynomial

The implementation uses the standard Ethernet CRC-32 generator polynomial:

```
100000100110000010001110110110111
```
