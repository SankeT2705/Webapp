from sklearn.metrics import accuracy_score, precision_score
import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression
import seaborn as sns
import matplotlib.pyplot as pyt
import pandas as pd

matches = pd.read_csv("matches.csv", index_col=0)
matches.head()
matches.shape
matches["team"].value_counts()
matches["round"].value_counts()
matches.dtypes
matches["date"] = pd.to_datetime(matches["date"])
matches["venue_code"] = matches["venue"].astype("category").cat.codes
matches["opp_code"] = matches["opponent"].astype("category").cat.codes
matches["team_code"] = matches["team"].astype("category").cat.codes
matches["hour"] = matches["time"].str.replace(
    ":.+", "", regex=True).astype("int")
matches["day_code"] = matches["day"].astype("category").cat.codes
# %% [markdown]
# 0 Thu
# 1 Fri
# 2 Sat
# 3 Sun
# 4 Mon
# 5 Tue
# 6 Wed
#
matches["target"] = (matches["result"] == 'W').astype("int")

# %% [markdown]
# 0 Draw & Lose
# 1 Win

# %%
team = matches.loc[matches.team == "Manchester City"]
cor = team.corr().round(2)
pyt.figure(figsize=(10, 8))
plot = sns.heatmap(team.corr().round(2), annot=True)

model = LogisticRegression(random_state=1)
train = matches[matches["date"] < '2022-1-1']
test = matches[matches["date"] > '2022-1-1']
predictors = ["venue_code", "team_code", "opp_code",
              "hour", "day_code", "xg", "xga", "gf"]
x = model.fit(train[predictors].values, train["target"])

preds = model.predict(test[predictors].values)
accuracy_score(test["target"], preds)
precision_score(test["target"], preds)
file = "Final.pkl"
pickle.dump(model, open(file, 'wb'))
load = pickle.load(open(file, 'rb'))


def predict(team1, team2, arg1, arg2, arg3, arg4, arg5, arg6):
    arr = np.array([team1, team2, arg1, arg2, arg3, arg4, arg5, arg6])
    result = load.predict(arr.reshape(1, -1))
    if result[0] == 1:
        return "Your Team Win"
    else:
        return "Your Team Lose/Draw"
