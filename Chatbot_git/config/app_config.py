n_gpu_layers = 1  # Metal set to 1 is enough.
n_batch = 512  # Should be between 1 and n_ctx, consider the amount of RAM of your Apple Silicon Chip.
B_INST,E_INST="[INST]","[/INST]"
n_ctx = 4096
n_batch = 2048