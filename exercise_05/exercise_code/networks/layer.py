import numpy as np


class Sigmoid:
    def __init__(self):
        pass

    def forward(self, x):
        """
        :param x: Inputs, of any shape

        :return out: Output, of the same shape as x
        :return cache: Cache, for backward computation, of the same shape as x
        """
        shape = x.shape
        outputs, cache = np.zeros(shape), np.zeros(shape)
        ########################################################################
        # TODO:                                                                #
        # Implement the forward pass of Sigmoid activation function            #
        ########################################################################

        pass
        cache = x
        outputs = [1 / (1 + np.e ** -i) for i in x]
        outputs = np.array(outputs)

        ########################################################################
        #                           END OF YOUR CODE                           #
        ########################################################################
        return outputs, cache

    def backward(self, dout, cache):
        """
        :return: dx: the gradient w.r.t. input X, of the same shape as X
        """
        dx = None
        ########################################################################
        # TODO:                                                                #
        # Implement the backward pass of Sigmoid activation function           #
        ########################################################################

        pass
        sig = np.array([1 / (1 + np.e ** -i) for i in cache])
        dx = sig * (1 - sig)
        # dx = [(1 / (1+np.e ** -i))*(1-(1 / (1+np.e ** -i))) for i in dout]
        dx = dx * dout
        dx = np.array(dx)
        print(dx.shape)
        print(cache.shape)

        ########################################################################
        #                           END OF YOUR CODE                           #
        ########################################################################
        return dx


class Relu:
    def __init__(self):
        pass

    def forward(self, x):
        """
        :param x: Inputs, of any shape

        :return out: Output, of the same shape as x
        :return cache: Cache, for backward computation, of the same shape as x
        """
        outputs = None
        cache = None
        ########################################################################
        # TODO:                                                                #
        # Implement the forward pass of Relu activation function               #
        ########################################################################

        pass
        cache = x
        z = np.zeros(x.shape)
        outputs = np.maximum(x, z)

        ########################################################################
        #                           END OF YOUR CODE                           #
        ########################################################################
        return outputs, cache

    def backward(self, dout, cache):
        """
        :return: dx: the gradient w.r.t. input X, of the same shape as X
        """
        dx = None
        ########################################################################
        # TODO:                                                                #
        # Implement the backward pass of Relu activation function              #
        ########################################################################

        pass
        dx = np.zeros(cache.shape)
        dx[np.where(cache > 0)] = 1
        dx = dx * dout

        ########################################################################
        #                           END OF YOUR CODE                           #
        ########################################################################
        return dx


def affine_forward(x, w, b):
    """
    Computes the forward pass for an affine (fully-connected) layer.
    The input x has shape (N, d_1, ..., d_k) and contains a minibatch of N
    examples, where each example x[i] has shape (d_1, ..., d_k). We will
    reshape each input into a vector of dimension D = d_1 * ... * d_k, and
    then transform it to an output vector of dimension M.
    Inputs:
    :param x: A numpy array containing input data, of shape (N, d_1, ..., d_k)
    :param w: A numpy array of weights, of shape (D, M)
    :param b: A numpy array of biases, of shape (M,)
    :return out: output, of shape (N, M)
    :return cache: (x, w, b)
    """
    cache = (x, w, b)
    N, M = x.shape[0], b.shape[0]
    out = np.zeros((N, M))
    ########################################################################
    # TODO: Implement the affine forward pass. Store the result in out.    #
    # You will need to reshape the input into rows.                        #
    ########################################################################

    pass
    x = x.reshape((x.shape[0], int(x.size / x.shape[0])))
    out = np.dot(x, w) + b

    ########################################################################
    #                           END OF YOUR CODE                           #
    ########################################################################

    return out, cache


def affine_backward(dout, cache):
    """
    Computes the backward pass for an affine layer.
    Inputs:
    :param dout: Upstream derivative, of shape (N, M)
    :param cache: Tuple of:
      - x: Input data, of shape (N, d_1, ... d_k)
      - w: Weights, of shape (D, M)
      - b: A numpy array of biases, of shape (M,
    :return dx: Gradient with respect to x, of shape (N, d1, ..., d_k)
    :return dw: Gradient with respect to w, of shape (D, M)
    :return db: Gradient with respect to b, of shape (M,)
    """
    x, w, b = cache
    dx, dw, db = None, None, None
    ########################################################################
    # TODO: Implement the affine backward pass.                            #
    # Hint: Don't forget to average the gradients dw and db                #
    ########################################################################

    pass
    dx = (dout.dot(w.T)).reshape(x.shape)  # N * D

    dw = x.reshape(x.shape[0], w.shape[0]).T.dot(dout) / dx.shape[0]  # D * M 和处以N求平均

    db = np.mean(dout.T, axis=1)  # M * 1
    #db = np.mean(dout, axis=0) 这句和上句在python里效果一样

    ########################################################################
    #                           END OF YOUR CODE                           #
    ########################################################################
    return dx, dw, db
