```python
import pandas as pd
import numpy as np

idx = pd.IndexSlice
```

#  Markdown section
words here!

## Method
More Words! 

```python
uam_none = pd.HDFStore('results/uam/long_none.h5', 'r')
uam_grs = pd.HDFStore('results/uam/grs.h5', 'r')

tally_num = 'tally_100014'
id = (10, 'err', 0)

fig, ax = plt.subplots(1, 2, sharey=False)

uam_tmc = mc.tmc_mean_stddev_df(uam_none[tally_num], )
uam_tmc['run'] = 0
uam_tmc = uam_tmc.reset_index().set_index(['cell', 'val_err', 'run'])

# only compare those values which stat err / obs err < 0.05
obs_var = uam_none[tally_num].loc[(10, 'val', slice(None)), :].var()
stat_var = (uam_none[tally_num].loc[(10, 'err', slice(None)), :]**2).sum() / len(uam_none[tally_num].loc[(10, 'err', slice(None)), :])
okay_err = stat_var ** 0.5 / obs_var ** 0.5 < 0.05
okay_err[-1] = False

max_box = 1
plot_rel_err_vs_other(uam_tmc.loc[:, okay_err], uam_grs[tally_num].loc[:, okay_err], id=id, ylabel="GRS Relative Error", max_box=max_box, ax=ax[0])
ax[0].set_title("238-Group Flux")

######################################################################################################

tally_num = 'tally_100024'
id = (10, 'err', 0)

uam_tmc = mc.tmc_mean_stddev_df(uam_none[tally_num], )
uam_tmc['run'] = 0
uam_tmc = uam_tmc.reset_index().set_index(['cell', 'val_err', 'run'])

# only compare those values which stat err / obs err < 0.05
obs_var = uam_none[tally_num].loc[(10, 'val', slice(None)), :].var()
stat_var = (uam_none[tally_num].loc[(10, 'err', slice(None)), :]**2).sum() / len(uam_none[tally_num].loc[(10, 'err', slice(None)), :])
okay_err = stat_var ** 0.5 / obs_var ** 0.5 < 0.05
okay_err[-1] = False

max_box = 1
plot_rel_err_vs_other(uam_tmc.loc[:, okay_err], uam_grs[tally_num].loc[:, okay_err], id=id, ylabel="", max_box=max_box, ax=ax[1])
ax[1].set_title("Reaction Rates")

ax[0].set(ylim=[0, max_box])
ax[1].set(xlim=[0, max_box])
plt.tight_layout()

save_many_ax(fig, ax, pad=0.05, savename_base='uam_fuel_rr')
```

    //anaconda/lib/python3.5/site-packages/mcnptallyreader/mc_stat_methods.py:356: RuntimeWarning: invalid value encountered in sqrt
      unstack_result_df.loc[:, idx[:, 'err']] = (obs_var.values - stat_var.values) ** 0.5



![png](output_5_1.png)

## Outputs Remain
Any outputs from python calls are still kept in this code. 

```python
    print(max_val, grs.columns[max_idx], max_idx, row[0])
    

```

    [ 0.] 1e-10 0 (0, 0, 'err', 0)
    [ 0.08375123] 6.0 85 (0, 1, 'err', 0)
    [ 0.19342033] 11.0 91 (0, 2, 'err', 0)
    [ 0.0942248] 2.3 76 (0, 3, 'err', 0)
    [ 0.07981539] 11.0 91 (0, 4, 'err', 0)
    [ 0.16670683] 12.0 92 (0, 5, 'err', 0)
    [ 0.08779032] 2.0 75 (0, 6, 'err', 0)
    [ 0.09062217] 12.0 92 (0, 7, 'err', 0)
    [ 0.09810253] 2.0 75 (0, 8, 'err', 0)
    [ 0.05449399] 3.3 79 (0, 9, 'err', 0)
    [ 0.06632017] 12.0 92 (0, 10, 'err', 0)
    [ 0.12011975] 2.0 75 (0, 11, 'err', 0)
    [ 0.0783511] 12.0 92 (0, 12, 'err', 0)
    [ 0.11681681] 11.0 91 (0, 13, 'err', 0)
    [ 0.06127719] 2.0 75 (0, 14, 'err', 0)
    [ 0.17130219] 1.8 74 (0, 15, 'err', 0)
    [ 0.14567069] 12.0 92 (0, 16, 'err', 0)
    [ 0.1013459] 12.0 92 (0, 17, 'err', 0)
    [ 0.12293977] 2.0 75 (0, 18, 'err', 0)
    [ 0.08405955] 2.3 76 (0, 19, 'err', 0)
    [ 0.09384502] 11.0 91 (0, 20, 'err', 0)
    [ 0.11854245] 2.9 78 (0, 21, 'err', 0)
    [ 0.11631462] 9.0 89 (0, 22, 'err', 0)
    [ 0.14698689] 5.5 84 (0, 23, 'err', 0)
    [ 0.11682138] 6.7 86 (0, 24, 'err', 0)
    [ 0.] 1e-10 0 (0, 25, 'err', 0)


    //anaconda/lib/python3.5/site-packages/ipykernel/__main__.py:11: RuntimeWarning: divide by zero encountered in true_divide
    //anaconda/lib/python3.5/site-packages/ipykernel/__main__.py:11: RuntimeWarning: invalid value encountered in true_divide
	