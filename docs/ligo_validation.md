# Validating Ringdown Predictions with LIGO/Virgo

1. Download GWTC-3 catalog:  
   `wget https://gwosc.org/eventapi/json/GWTC-3/`

2. Run comparison:  
   ```bash
   python entropy_simulations/ringdown_analysis.py --event GW150914 --tfm_model data/blackhole_ringdowns.h5
