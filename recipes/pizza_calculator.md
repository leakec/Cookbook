<div style="background: var(--md-code-bg-color, #f8f9fa); padding: 20px; border-radius: 8px; border: 1px solid #ddd; margin: 20px 0;">
  <form id="pizzaCalcForm" oninput="calculatePizza()">
    
    <label for="pizzaCount"><b>Number of Pizzas:</b></label><br>
    <input type="number" id="pizzaCount" value="2" min="1" step="1" style="width: 100%; padding: 8px; margin: 8px 0 16px;"><br>

    <label for="pizzaSize"><b>Pizza Size (Diameter in inches):</b></label><br>
    <input type="number" id="pizzaSize" value="14" min="1" step="0.1" style="width: 100%; padding: 8px; margin: 8px 0 16px;"><br>

  </form>
</div>

<script>
function calculatePizza() {
  // 1. Grab values from the inputs
  const count = parseInt(document.getElementById('pizzaCount').value, 10) || 0;
  const size = parseFloat(document.getElementById('pizzaSize').value) || 0;
  
  // 2. Perform the math operations
  const flour = 300.0 * count * Math.pow(size, 2) / ( 2 * Math.pow(14, 2))
  const salt = flour * 0.025
  const sugar = flour * 0.025
  const yeast = flour * 0.005
  const oil = flour * 0.1
  const water = flour * 0.5
  
  // 3. Inject inputs and outputs into different parts of the HTML
  document.getElementById('count').innerText = count;
  document.getElementById('flour').innerText = flour.toFixed(2);
  document.getElementById('salt').innerText = salt.toFixed(2);
  document.getElementById('sugar').innerText = sugar.toFixed(2);
  document.getElementById('yeast').innerText = yeast.toFixed(2);
  document.getElementById('oil').innerText = oil.toFixed(2);
  document.getElementById('water').innerText = water.toFixed(2);
}
</script>
