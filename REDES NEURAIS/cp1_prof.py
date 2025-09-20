def perceptron_training(inputs: list, weights: list, epochs: int, step_function_vl: int, outputs: list, learning_rate: int):

  converge = False

  for epoch in range(epochs):
    print()
    print(f" ----------------------------------------------------------------------- Época {epoch+1} ----------------------------------------------------------------------")

    # Loop nos inputs
    for item, input in enumerate(inputs):
      calculation = (input[0]*weights[0]) + (input[1]*weights[1])
      print(f"O cálculo dos inputs {input[0]}/{input[1]}, os pesos {weights[0]}/{weights[1]} dá {calculation}")

      # Step function
      if calculation >= step_function_vl:
        value = 1
      else:
        value = 0
      print(f"O resultado pós step é {value}")

      # Evaluation
      if value != outputs[item]:

        # Erro
        print("Erro")
        error   = outputs[item] - value
        print(f"O valor do erro é {error}")

        # New weights
        w0      = weights[0] + (learning_rate * input[0] * error)
        w1      = weights[1] + (learning_rate * input[1] * error)
        weights = []
        weights.append(w0)
        weights.append(w1)
        print(f"Os novos pesos são {w0}, {w1}")

      # Acertos e possível conversão
      else:
        if item == (len(inputs) - 1):
          print("A rede convergiu")
          converge = True
          break
    if converge:
      break
  
input   = [[0.5, 0.8], [0.2, 0.4]]
weights = [0.2, -0.1]
epochs  = 13
step_function_vl = 0
outputs = [1, 0]
learning_rate = 0.1

perceptron_training(input, weights, epochs, step_function_vl, outputs, learning_rate)