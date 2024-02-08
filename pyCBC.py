from pycbc.waveform import get_td_waveform
import matplotlib.pyplot as plt

# Assuming typical values for a binary black hole similar to GW150914
# mass1 and mass2 are the masses of the two black holes in solar masses
mass1 = 30
mass2 = 30

# distance in Mpc (megaparsecs)
distance = 410  # Approx distance to GW150914

# Specify the lower frequency bound
f_lower = 20  # The starting frequency of the waveform

# Generate the waveform
hp, hc = get_td_waveform(approximant='SEOBNRv4_opt',
                         mass1=mass1,
                         mass2=mass2,
                         delta_t=1.0/4096,
                         f_lower=f_lower,
                         distance=distance)

# Plotting the plus polarization of the waveform
plt.figure(figsize=(10, 6))
plt.plot(hp.sample_times, hp, label='h+ (Plus polarization)')
plt.xlabel('Time (s)')
plt.ylabel('Strain')
plt.title('Gravitational Wave Time-Domain Waveform')
plt.legend()
plt.grid(True)
plt.show()
