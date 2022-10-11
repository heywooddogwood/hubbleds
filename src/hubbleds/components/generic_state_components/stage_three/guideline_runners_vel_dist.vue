<template>
  <scaffold-alert
    header-text="Runners' Velocities vs. Distances"
    @back="() => {
      state.marker = 'run_rac1';
      state.race_dialog = true
    }"
    @next="
      state.marker = 'age_uni1';
    "
  >
    <div
      class="mb-4"
    >
      <p>
        To return to this data story, if we graph the runners’ velocities vs. distance, the graph would look like this.
      </p>
      <p>
        Doesn’t this look a lot like your graph for the galaxies?
      </p>
    </div>
  </scaffold-alert>
</template>
