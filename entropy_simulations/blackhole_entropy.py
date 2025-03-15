import numpy as np
from scipy.integrate import solve_ivp

def bh_entropy_correction(M, lambda_tfm=1.2e-5, gamma=0.45):
    """TFM-modified Bekenstein-Hawking entropy (Eq. 6.1)"""
    S_classic = 4 * np.pi * M**2  # In natural units (G=c=ħ=1)
    delta_S = lambda_tfm * gamma * np.sqrt(M) * np.log(M)
    return S_classic + delta_S

# Calculate entropy for M87* (6.5e9 solar masses)
M_m87 = 6.5e9  
S_tfm = bh_entropy_correction(M_m87)
print(f"TFM entropy for M87*: {S_tfm:.2e} (vs classical {4*np.pi*M_m87**2:.2e})")
