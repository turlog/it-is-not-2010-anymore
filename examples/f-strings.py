import numpy

rnd = numpy.random.rand(20)

print(
    "Got {} measurements between {:.1f} and "
    "{:.1f} with a mean value of {:.2f}.".format(
        len(rnd), rnd.min(), rnd.max(), rnd.mean()
    )
)

print(
    f"Got {len(rnd)} measurements between {rnd.min():.1f} and "
    f"{rnd.max():.1f} with a mean value of {rnd.mean():.2f}."
)
