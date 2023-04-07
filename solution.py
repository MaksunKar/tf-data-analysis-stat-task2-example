import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 790154026 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    mean1 = 2 / 89 ** 2 * (gamma.ppf((1 - p) / 2, x.size) / x.size + x.mean() - 1 / 2)
    mean2 = 2 / 89 ** 2 * (gamma.ppf((1 + p) / 2, x.size) / x.size + x.mean() - 1 / 2)
    return mean1, mean2
