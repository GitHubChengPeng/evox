from evox import algorithms, problems, workflows
import jax
import jax.numpy as jnp

algorithm = algorithms.PSO(
    lb=jnp.full(shape=(2,), fill_value=-32),
    ub=jnp.full(shape=(2,), fill_value=32),
    pop_size=100,
)

problem = problems.numerical.Ackley()

# create a pipeline

pipeline = workflows.StdPipeline(
    algorithm,
    problem,
)

# init the pipeline
key = jax.random.PRNGKey(42)
state = pipeline.init(key)

# run the pipeline for 100 steps
for i in range(100):
    state = pipeline.step(state)
