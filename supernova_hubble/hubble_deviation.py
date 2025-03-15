import astropy.units as u
from astropy.cosmology import Planck18

def tfm_hubble_deviation(z, S_ratio=0.15):
    """Computes δ_μ(z) from entropy-driven expansion (Eq. 6.2)"""
    mu_lcdm = Planck18.distmod(z).value
    delta_mu = S_ratio * np.log(1 + z) * (1 - np.exp(-z/0.5))
    return mu_lcdm + delta_mu

# Compare at z=0.7 (critical for DES survey)
z = 0.7
print(f"Δμ(z=0.7) = {tfm_hubble_deviation(z) - Planck18.distmod(z).value:.3f} mag")
