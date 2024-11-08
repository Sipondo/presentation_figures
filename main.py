import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

FRAME_COUNT = 5

# Slide 1

x = (np.random.rand(50) - 0.5) * 2
y = (np.random.rand(50) - 0.5) * 2

z = y > 0

species = pd.Series(z)

species[z] = "dog"
species[~z] = "cat"

data = pd.DataFrame(list(zip(x, y, species)), columns=["x", "y", "species"])

pal = dict(cat="#6495ED", dog="#F08080")

plot = sns.scatterplot(
    x="x",
    y="y",
    hue="species",
    palette=pal,  # palette="ch:r=-.2,d=.3_r",
    sizes=(1, 8),
    linewidth=0,
    data=data,
)

plot.axes.xaxis.set_ticklabels([])
plot.axes.yaxis.set_ticklabels([])
plot.set_xlabel("Age")
plot.set_ylabel("Herd Instinct")

plt.savefig("nn1.svg")
plt.show()
data.to_csv("nn1.csv")

# Slide 1 Solution

# x = (np.random.rand(50)-0.5)*2
# y = (np.random.rand(50)-0.5)*2

z = y > 0

species = pd.Series(z)

species[z] = "dog"
species[~z] = "cat"

data = pd.DataFrame(list(zip(x, y, species)), columns=["x", "y", "species"])

pal = dict(cat="#6495ED", dog="#F08080")

plot = sns.scatterplot(
    x="x",
    y="y",
    hue="species",
    palette=pal,  # palette="ch:r=-.2,d=.3_r",
    sizes=(1, 8),
    linewidth=0,
    data=data,
)

plot.axes.xaxis.set_ticklabels([])
plot.axes.yaxis.set_ticklabels([])
plot.set_xlabel("Age")
plot.set_ylabel("Herd Instinct")

plot.axhline(color="orange")

plt.savefig("nn1_sol.svg")
plt.show()

##############################################################################
##############################################################################
##############################################################################
# Slide 2

x = (np.random.rand(150) - 0.5) * 2
y = (np.random.rand(150) - 0.5) * 2

z = (y > 0) & (x > 0)

species = pd.Series(z)

species[z] = "dog"
species[~z] = "cat"

data = pd.DataFrame(list(zip(x, y, species)), columns=["x", "y", "species"])

data.y = data.y - data.x

pal = dict(cat="#6495ED", dog="#F08080")

plot = sns.scatterplot(
    x="x",
    y="y",
    hue="species",
    palette=pal,  # palette="ch:r=-.2,d=.3_r",
    sizes=(1, 8),
    linewidth=0,
    data=data,
)

plot.axes.xaxis.set_ticklabels([])
plot.axes.yaxis.set_ticklabels([])
plot.set_xlabel("X")
plot.set_ylabel("Y")

# plot.axhline(color="orange")

plt.savefig("nn2.svg")
plt.show()
data.to_csv("nn2.csv")

old_data = data

# Slide 2.1.anim

for frame in range(1, FRAME_COUNT):
    z = (y > 0) & (x > 0)

    species = pd.Series(z)

    species[z] = "dog"
    species[~z] = "cat"

    data = pd.DataFrame(list(zip(x, y, species)), columns=["x", "y", "species"])

    data.x = (data.x * frame + old_data.x * (FRAME_COUNT - frame)) / FRAME_COUNT
    data.y = (data.y * frame + old_data.y * (FRAME_COUNT - frame)) / FRAME_COUNT

    pal = dict(cat="#6495ED", dog="#F08080")

    plot = sns.scatterplot(
        x="x",
        y="y",
        hue="species",
        palette=pal,  # palette="ch:r=-.2,d=.3_r",
        sizes=(1, 8),
        linewidth=0,
        data=data,
    )

    plot.axes.xaxis.set_ticklabels([])
    plot.axes.yaxis.set_ticklabels([])
    plot.set_xlabel("-")
    plot.set_ylabel("-")

    # plot.axhline(color="orange")

    plt.savefig(f"nn2.1.anim.{frame}.svg")
    print("Frame:", frame)
    plt.show()

# Slide 2.1

z = (y > 0) & (x > 0)

species = pd.Series(z)

species[z] = "dog"
species[~z] = "cat"

data = pd.DataFrame(list(zip(x, y, species)), columns=["x", "y", "species"])


pal = dict(cat="#6495ED", dog="#F08080")

plot = sns.scatterplot(
    x="x",
    y="y",
    hue="species",
    palette=pal,  # palette="ch:r=-.2,d=.3_r",
    sizes=(1, 8),
    linewidth=0,
    data=data,
)

plot.axes.xaxis.set_ticklabels([])
plot.axes.yaxis.set_ticklabels([])
plot.set_xlabel("-")
plot.set_ylabel("-")

# plot.axhline(color="orange")

plt.savefig("nn2.1.svg")
plt.show()
data.to_csv("nn2.1.csv")

# Slide 2.2


z = (y > 0) & (x > 0)

species = pd.Series(z)

species[z] = "dog"
species[~z] = "cat"

data = pd.DataFrame(list(zip(x, y, species)), columns=["x", "y", "species"])


pal = dict(cat="#6495ED", dog="#F08080")

plot = sns.scatterplot(
    x="x",
    y="y",
    hue="species",
    palette=pal,  # palette="ch:r=-.2,d=.3_r",
    sizes=(1, 8),
    linewidth=0,
    data=data,
)

plot.axes.xaxis.set_ticklabels([])
plot.axes.yaxis.set_ticklabels([])
plot.set_xlabel("-")
plot.set_ylabel("-")

plot.axhline(color="green")
plot.axvline(color="orange")


plt.savefig("nn2.2.svg")
plt.show()
data.to_csv("nn2.2.csv")

old_data = data


# Slide 2.3.anim
def sigmoid(z):
    return 1 / (1 + np.exp(-z))


for frame in range(1, FRAME_COUNT):

    z = (y > 0) & (x > 0)

    species = pd.Series(z)

    species[z] = "dog"
    species[~z] = "cat"

    data = pd.DataFrame(
        # list(zip(2 * (x > 0) - 1, 2 * (y > 0) - 1, species)),
        list(zip(sigmoid(x * 100), sigmoid(y * 100), species)),
        columns=["x", "y", "species"],
    )

    data.x = (data.x * frame + old_data.x * (FRAME_COUNT - frame)) / FRAME_COUNT
    data.y = (data.y * frame + old_data.y * (FRAME_COUNT - frame)) / FRAME_COUNT

    pal = dict(cat="#6495ED", dog="#F08080")

    plot = sns.scatterplot(
        x="x",
        y="y",
        hue="species",
        palette=pal,  # palette="ch:r=-.2,d=.3_r",
        sizes=(1, 8),
        linewidth=0,
        data=data,
    )

    plot.axes.xaxis.set_ticklabels([])
    plot.axes.yaxis.set_ticklabels([])
    plot.set_xlabel("-")
    plot.set_ylabel("-")

    plt.savefig(f"nn2.3.anim.{frame}.svg")
    print("Frame:", frame)
    plt.show()


# Slide 2.3


# z = (y > 0) & (x > 0)

# species = pd.Series(z)

# species[z] = "dog"
# species[~z] = "cat"

# data = pd.DataFrame(
#     list(zip(2 * (x > 0) - 1, 2 * (y > 0) - 1, species)), columns=["x", "y", "species"]
# )

data = pd.DataFrame(
    # list(zip(2 * (x > 0) - 1, 2 * (y > 0) - 1, species)),
    list(zip(sigmoid(x * 100), sigmoid(y * 100), species)),
    columns=["x", "y", "species"],
)

x = sigmoid(x * 100)
y = sigmoid(y * 100)


pal = dict(cat="#6495ED", dog="#F08080")

plot = sns.scatterplot(
    x="x",
    y="y",
    hue="species",
    palette=pal,  # palette="ch:r=-.2,d=.3_r",
    sizes=(1, 8),
    linewidth=0,
    data=data,
)

plot.axes.xaxis.set_ticklabels([])
plot.axes.yaxis.set_ticklabels([])
plot.set_xlabel("A")
plot.set_ylabel("B")


plt.savefig("nn2.3.svg")
plt.show()
data.to_csv("nn2.3.csv")


# # prep
# xf = np.array([-1, -1, 1, 1])
# yf = np.array([-1, 1, 1, -1])

# z = xf > 0

# species = pd.Series(z)

# species[z] = "dog"
# species[~z] = "cat"

old_data = pd.DataFrame(list(zip(x, y, species)), columns=["x", "y", "species"])

# Slide 2.4 anim

rotation_matrix = np.array(((2**0.5 / 2, -(2**0.5 / 2)), (2**0.5 / 2, 2**0.5 / 2)))

for frame in range(1, FRAME_COUNT):

    # xf = np.array([-1.5, -0.5, 0.5, -0.5])
    # yf = np.array([0, 0.5, 0, -0.5])

    # z = xf > 0

    # species = pd.Series(z)

    # species[z] = "dog"
    # species[~z] = "cat"

    # data = pd.DataFrame(list(zip(xf, yf, species)), columns=["x", "y", "species"])
    values = np.stack((old_data.x, old_data.y), axis=0)
    result = np.dot(rotation_matrix, values)
    data.x = result[0]
    data.y = result[1]

    data.x = (data.x * frame + old_data.x * (FRAME_COUNT - frame)) / FRAME_COUNT
    data.y = (data.y * frame + old_data.y * (FRAME_COUNT - frame)) / FRAME_COUNT

    pal = dict(cat="#6495ED", dog="#F08080")

    plot = sns.scatterplot(
        x="x",
        y="y",
        hue="species",
        palette=pal,  # palette="ch:r=-.2,d=.3_r",
        sizes=(1, 8),
        linewidth=0,
        data=data,
    )

    plot.axes.xaxis.set_ticklabels([])
    plot.axes.yaxis.set_ticklabels([])
    plot.set_xlabel("-")
    plot.set_ylabel("-")

    plt.savefig(f"nn2.4.anim.{frame}.svg")
    print("Frame:", frame)
    plt.show()


# Slide 2.4

# xf = np.array([-1.5, -0.5, 0.5, -0.5])
# yf = np.array([0, 0.5, 0, -0.5])

# z = xf > 0

# species = pd.Series(z)

# species[z] = "dog"
# species[~z] = "cat"

# data = pd.DataFrame(list(zip(xf, yf, species)), columns=["x", "y", "species"])
values = np.stack((old_data.x, old_data.y), axis=0)
result = np.dot(rotation_matrix, values)
data.x = result[0]
data.y = result[1]


pal = dict(cat="#6495ED", dog="#F08080")

plot = sns.scatterplot(
    x="x",
    y="y",
    hue="species",
    palette=pal,  # palette="ch:r=-.2,d=.3_r",
    sizes=(1, 8),
    linewidth=0,
    data=data,
)

plot.axes.xaxis.set_ticklabels([])
plot.axes.yaxis.set_ticklabels([])
plot.set_xlabel("-")
plot.set_ylabel("-")


plt.savefig("nn2.4.svg")
plt.show()
data.to_csv("nn2.4.csv")


# Slide 2.5

# xf = np.array([-1.5, -0.5, 0.5, -0.5])
# yf = np.array([0, 0.5, 0, -0.5])

# z = xf > 0

# species = pd.Series(z)

# species[z] = "dog"
# species[~z] = "cat"

# data = pd.DataFrame(list(zip(xf, yf, species)), columns=["x", "y", "species"])


pal = dict(cat="#6495ED", dog="#F08080")

plot = sns.scatterplot(
    x="x",
    y="y",
    hue="species",
    palette=pal,  # palette="ch:r=-.2,d=.3_r",
    sizes=(1, 8),
    linewidth=0,
    data=data,
)

plot.axes.xaxis.set_ticklabels([])
plot.axes.yaxis.set_ticklabels([])
plot.set_xlabel("-")
plot.set_ylabel("-")
plot.axvline(color="orange")

plt.savefig("nn2.5.svg")
plt.show()
data.to_csv("nn2.5.csv")
