import math
import random

class Qubit:
    def __init__(self, alpha=1.0, beta=0.0):
        # Нормировка амплитуд
        norm = math.sqrt(abs(alpha)**2 + abs(beta)**2)
        self.alpha = alpha / norm
        self.beta = beta / norm

    def __str__(self):
        return f"[{self.alpha:.3f}|0⟩ + {self.beta:.3f}|1⟩]"

    def measure(self):
        # Измерение кубита (вероятностное)
        prob_0 = abs(self.alpha)**2
        return 0 if random.random() < prob_0 else 1

# --- Гейты Паули ---
def apply_x(qubit):
    new_alpha = qubit.beta
    new_beta = qubit.alpha
    return Qubit(new_alpha, new_beta)

def apply_y(qubit):
    new_alpha = -1j * qubit.beta
    new_beta = 1j * qubit.alpha
    return Qubit(new_alpha, new_beta)

def apply_z(qubit):
    new_alpha = qubit.alpha
    new_beta = -qubit.beta
    return Qubit(new_alpha, new_beta)

# --- Двухкубитный гейт CNOT (исправленный) ---
def apply_cnot(control, target):
    # CNOT без измерения (унитарное преобразование)
    # Если control = |1⟩, инвертируем target
    new_target_alpha = control.alpha * target.beta + control.beta * target.alpha
    new_target_beta = control.alpha * target.alpha + control.beta * target.beta
    return (control, Qubit(new_target_alpha, new_target_beta))

# --- Демонстрация ---
if __name__ == "__main__":
    # Создаём кубиты
    q1 = Qubit(1, 0)  # control = |0⟩
    q2 = Qubit(1, 0)  # target = |0⟩
    print("До CNOT: control =", q1, ", target =", q2)
    q1, q2 = apply_cnot(q1, q2)
    print("После CNOT (control=|0⟩): control =", q1, ", target =", q2)

    q1 = apply_x(q1)  # control = |1⟩
    q1, q2 = apply_cnot(q1, Qubit(1, 0))  # target снова |0⟩
    print("После CNOT (control=|1⟩): control =", q1, ", target =", q2)