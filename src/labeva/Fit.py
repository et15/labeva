import lmfit
import mathfunc


# === Fit function & model ===
# linear function
lin = lmfit.Model(mathfunc.lin)
lin_params = lin.make_params(
    m={"value": 1, "min": -10, "max": 10}, b={"value": 0, "min": -10, "max": 10}
)


# exponential function
exp_decay = lmfit.Model(mathfunc.exp_decay)
exp_decay_params = exp_decay.make_params(
    tau={"value": 15, "min": 0, "max": 500},
    a={"value": 0.25, "min": 0, "max": 5},
    b={"value": 0, "min": -5, "max": 5},
)


# gaussian
gauss = lmfit.Model(mathfunc.gauss)
gauss_params = gauss.make_params(
    mu={"value": 0}, sigma={"value": 1}, a0={"value": 1}, b={"value": 0}
)

gauss_normalized = lmfit.Model(mathfunc.gauss_normalized)
gauss_normalized_params = gauss_normalized.make_params(
    mu={"value": 0}, sigma={"value": 1}
)
