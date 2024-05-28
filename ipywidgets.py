import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import streamlit as st

# Set Streamlit page layout to wide
st.set_page_config(layout="wide")

# Calculate theoretical quantiles for the forecasted distribution once
theoretical_quantiles = (np.arange(1, 1001) - 0.5) / 1000
# Using the theoretical quantiles to generate the forecasted distribution
forecasted = stats.norm.ppf(theoretical_quantiles, 0, 1)

def update_plot(mu_obs, sigma_obs):
    np.random.seed(0)  # For reproducibility

    # Simulating the observed distribution
    observed = np.random.normal(mu_obs, sigma_obs, 500)

    # Calculate u-values
    u_values = stats.norm.cdf(observed, 0, 1)

    # Create the figure and axes for three plots
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(30, 10))  # Increase the figsize

    # Create bins suitable for both distributions
    combined_data = np.hstack([forecasted, observed])
    bins = np.histogram_bin_edges(combined_data, bins='auto')

    # Histogram of observed points
    ax1.hist(observed, bins=bins, density=True, alpha=0.6, color='red', label='Observed')

    # Overlay of theoretical normal distribution for observed
    best_fit_line = stats.norm.pdf(bins, 0, 1)
    ax1.plot(bins, best_fit_line, 'k--', linewidth=2, label='Forecast Distribution')

    # Set up the plot
    ax1.set_title('Comparison of Forecasted and Observed Distributions')
    ax1.set_xlabel('Value')
    ax1.set_ylabel('Density')
    ax1.legend()

    # Histogram of u-values
    ax2.hist(u_values, bins=10, range=(0, 1), alpha=0.75, color='blue')
    ax2.set_title('Histogram of u-values')
    ax2.set_xlabel('u-values')
    ax2.set_ylabel('Frequency')

    # Calculate u-values and sort them
    u_sorted = np.sort(u_values)

    # Calculate lj and Dc-vM
    N = len(u_sorted)
    j = np.arange(1, N+1)
    lj = (2 * j - 1) / (2 * N)
    Dc_vM = (1/N) * (1 / (12 * N) + np.sum((u_sorted - lj)**2))

    # Plot of pj and lj
    ax3.scatter(j, u_sorted, color='blue', label='pj (Sorted u-values)')
    ax3.scatter(j, lj, color='red', alpha=0.6, label='lj (Expected positions)')
    ax3.set_title(f'Cramér – von Mises Plot (Dc-vM: {Dc_vM:.4f})')
    ax3.set_xlabel('Index (j)')
    ax3.set_ylabel('Percent')
    ax3.legend()

    plt.tight_layout()
    st.pyplot(fig)

# Streamlit widgets for user input
st.title("Interactive Plot for Linear Trades and Risk Quantification")

mu_obs = st.slider('Mu Obs:', min_value=-2.0, max_value=2.0, value=0.0, step=0.5)
sigma_obs = st.slider('Sigma Obs:', min_value=0.25, max_value=2.0, value=1.0, step=0.25)

update_plot(mu_obs, sigma_obs)
