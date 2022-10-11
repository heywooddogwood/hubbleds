<template>
  <scaffold-alert
    header-text="Hubble's Expanding Universe"
    @back="
      state.marker = 'hub_exp1';
    "
    @next="
      state.marker = 'run_rac1';
      state.race_dialog = true;
    "
  >
    <div
      class="mb-4"
    >
      <p>
        This was a <strong>huge</strong> deal in 1929. This relationship that Hubble found serves as evidence that we live in an <strong>expanding universe</strong>. Hubble realized that an expanding universe implies that at some point all the galaxies were much closer together — "<strong>The Big Bang</strong>". The amount of time since The Big Bang tells us the <strong>age of the universe</strong>.
      </p>
    </div>
  </scaffold-alert>
</template>
