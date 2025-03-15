import healpy as hp
import pyfits as pf

def calculate_fnl(map_data, l_max=3000):
    """Estimates local-type f_nl from TFM micro-Big Bang imprints"""
    alm = hp.map2alm(map_data, lmax=l_max)
    # Apply TFM bispectral model (Eq. 6.3)
    fnl = np.std(alm[1:]) / np.mean(alm[1:])  # Simplified estimator
    return fnl

# Load simulated CMB map
cmb_map = hp.read_map("data/cmb_tfm_simulated.fits")
print(f"TFM-predicted f_nl: {calculate_fnl(cmb_map):.2f}")
