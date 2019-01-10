# systemspecs
Prints GPU, CPU, RAM, storage, etc. for linux/unix systems.

## Usage

### Using terminal:
```bash
$ ./system_specs.py
```
### Using Python:
```bash
$ python system_specs.py
```

### Using Jupyter Notebook:
Run [this notebook](https://github.com/cgnorthcutt/systemspecs/blob/master/system_specs.ipynb).

## Example output


**OS**: Linux Debian 4.9.130-2 (2018-10-27)

**Architecture**: 64bit , x86_64

**Storage**: 219 GB

**RAM**: 24 GB

**Num CPU**: 12

**Num GPU**: 2

**GPU Information:**

Thu Jan 10 21:25:07 2019       

| NVIDIA-SMI 410.72 |           |      |               | Driver Version: 410.72 |        | CUDA Version: 10.0 |             |
|-------------------|-----------|------|---------------|------------------------|--------|--------------------|-------------|
| GPU               | Name      |      | Persistence   | Bus-Id                 | Disp.A | Volatile           | Uncorr. ECC |
| Fan               | Temp      | Perf | Pwr:Usage/Cap | Memory-Usage           |        | GPU-Util           | Compute M.  |
| 0                 | Tesla K80 |      | Off           | 00000000:00:04.0       | Off    |                    | 0           |
| N/A               | 45C       | P8   | 28W / 149W    | 0MiB / 11441MiB        |        | 0%                 | Default     |
| 1                 | Tesla K80 |      | Off           | 00000000:00:05.0       | Off    |                    | 0           |
| N/A               | 42C       | P8   | 42W / 149W    | 0MiB / 11441MiB        |        | 0%                 | Default     |


# License
MIT License. 
