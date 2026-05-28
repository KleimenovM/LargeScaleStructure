import numpy as np

TIME_FERMI = np.datetime64('2008-08-08T15:43:36')
FERMI_TIMESTAMP = 239760269

def time_fermi_to_utc(t: float):
    dif = np.array(t - FERMI_TIMESTAMP, dtype="m8[s]")  # difference in seconds
    data = TIME_FERMI + dif
    return data


if __name__ == "__main__":
    print("Not for direct use.")
