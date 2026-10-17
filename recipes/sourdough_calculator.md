<div style="background: var(--md-code-bg-color, #f8f9fa); padding: 20px; border-radius: 8px; border: 1px solid #ddd; margin: 20px 0;">
  <form id="sourdoughCalcForm" oninput="calculateSourdough()">
    
    <label for="numLoaves"><b>Number of loaves:</b></label><br>
    <input type="number" id="numLoaves" value="1" min="1" step="1" style="width: 100%; padding: 8px; margin: 8px 0 16px;"><br>

    <label for="totFlour"><b>Total flour:</b></label><br>
    <input type="number" id="totFlour" value="500" min="1" step="1" style="width: 100%; padding: 8px; margin: 8px 0 16px;"><br>

  </form>
</div>

<script>
function calculateSourdough() {
  // 1. Grab values from the inputs
  const count = parseInt(document.getElementById('numLoaves').value, 10) || 0;
  const totFlour = parseFloat(document.getElementById('totFlour').value) || 0;
  
  // 2. Perform the math operations
  const flour = count * totFlour
  const breadFlour = flour / 2.0
  const wheatFlour = flour / 2.0
  const water = flour * 0.75
  const starter = flour * 0.2
  const salt = flour * 0.02
  
  // 3. Inject inputs and outputs into different parts of the HTML
  document.getElementById('breadFlour').innerText = breadFlour.toFixed(2);
  document.getElementById('wheatFlour').innerText = wheatFlour.toFixed(2);
  document.getElementById('water').innerText = water.toFixed(2);
  document.getElementById('starter').innerText = starter.toFixed(2);
  document.getElementById('salt').innerText = salt.toFixed(2);
}
</script>
