# Windows Process Forensics Sampler

A Python utility using `psutil` designed for digital forensics and incident response (DFIR). It inspects active system processes, randomly selects a running target, and extracts detailed operational metadata, resource usage, and network activity for rapid initial triage.

## Features

* **PID Enumeration**: Lists all active process IDs running on the system.
* **Random Process Sampling**: Selects a target process for isolated inspection.
* **Process Metadata Extraction**: Retrieves executable path, working directory, command-line arguments, parent/child relationships, user context, and creation time.
* **Resource Monitoring**: Analyzes CPU consumption, CPU accumulated times, memory usage percentage, and detailed memory metrics.
* **Network Connection Mapping**: Enumerates active `inet` socket connections with status, local source, and remote destination details.

## Prerequisites

* Python 3.x
* `psutil` library

Install dependencies:
```bash
pip install psutil