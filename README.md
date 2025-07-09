# bms-frame-sagemanifold
This SageMath script implements the Bondi-Sachs metric for asymptotically flat vacuum spacetimes, following the framework outlined by Mitman et al.([Computation of displacement and spin gravitational memory in numerical relativity](https://arxiv.org/abs/2007.11562)). It follows the Bondi formalism, focusing on vacuum solutions near future null infinity with retarded Bondi coordinates.

Important Notes:

Asymptotic expansions Equation (12-15) are not implemented yet, but the code’s structure supports future inclusion of expansions for the Bondi mass aspect, angular momentum aspect, share, etc.


Future Extensions

This code is designed to be extended with:
1. Asymptotic expansions of metric functions, incorporating Bondi mass aspect, angular momentum aspect, shear tensor, and their evolution.
2. Computations of non linear memory effects

What is Bondi-Sachs formalism? (http://arxiv.org/abs/1609.01731)

The Bondi-Sachs formalism of General Relativity is a metric-based treatment of the Einstein equations in which the coordinates are adapted to the null geodesics of the spacetime. It provided the first convincing evidence that gravitational radiation is a nonlinear effect of general relativity and that the emission of gravitational waves from an isolated system is accompanied by a mass loss from the system. The asymptotic behaviour of the Bondi-Sachs metric revealed the existence of the symmetry group at null infinity, the Bondi-Metzner-Sachs group, which turned out to be larger than the Poincare group.
