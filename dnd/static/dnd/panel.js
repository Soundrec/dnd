const seed_value = document.querySelector("#seed_value");
const seed_input = document.querySelector("#seed_input");
seed_input.value = 1;
seed_value.textContent = seed_input.value;

seed_input.addEventListener("input", (event) => {
  seed_value.textContent = event.target.value;
});

const lora_alpha_value = document.querySelector("#lora_alpha_value");
const lora_alpha_input = document.querySelector("#lora_alpha_input");
lora_alpha_input.value = 6;
lora_alpha_value.textContent = lora_alpha_input.value;

lora_alpha_input.addEventListener("input", (event) => {
  lora_alpha_value.textContent = event.target.value;
});

const tmp_value = document.querySelector("#tmp_value");
const tmp_input = document.querySelector("#tmp_input");
tmp_input.value = 1.1;
tmp_value.textContent = tmp_input.value;

tmp_input.addEventListener("input", (event) => {
  tmp_value.textContent = event.target.value;
});

const mnt_value = document.querySelector("#mnt_value");
const mnt_input = document.querySelector("#mnt_input");
mnt_input.value = 128;
mnt_value.textContent = mnt_input.value;

mnt_input.addEventListener("input", (event) => {
  mnt_value.textContent = event.target.value;
});